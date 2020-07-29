from flask import (Flask, render_template, request,
                   redirect, url_for, flash)
import os
import uuid
import sightings
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('secret_key')

ufo_shapes = {
    "cigar": "Cigar shaped",
    "saucer": "Suacer shaped",
    "ball": "Ball shaped",
    "others": "Other shapes"
}


# global variable
database = sightings.load()


@app.route('/')
def show_all_sightings():
    return render_template("all_sightings.template.html", database=database)


@app.route('/create-sighting')
def show_create_sighting_form():
    return render_template("sighting_form.template.html", sighting={},
                           ufo_shapes=ufo_shapes)


@app.route('/create-sighting', methods=["POST"])
def process_create_sighting_form():

    next_id = str(uuid.uuid1())

    sighting = sightings.create_sighting(next_id, request)

    database[next_id] = sighting
    sightings.save(database)
    flash(f"ID added: {next_id}")
    flash(f"New sighting created: {request.form.get('title')}")

    return redirect(url_for("show_all_sightings"))


@app.route('/edit-sighting/<sighting_id>')
def show_edit_sighting_form(sighting_id):
    sighting = database.get(sighting_id)
    if sighting is None:
        return "Not found. ID does not exist"

    return render_template('edit_sighting.template.html', sighting=sighting,
                           ufo_shapes=ufo_shapes)


@app.route('/edit-sighting/<sighting_id>', methods=["POST"])
def edit_sighting(sighting_id):
    sighting = sightings.get_by_id(database, sighting_id)
    if sighting is None:
        return "Not found. ID does not exist"

    sighting = sightings.create_sighting(sighting_id, request)

    database[sighting_id] = sighting

    sightings.save(database)
    flash(f"Sighting with the id of {sighting_id} has been modified")

    return redirect(url_for("show_all_sightings"))


@app.route('/delete-sighting/<sighting_id>')
def show_delete_confirmation(sighting_id):
    # sighting = database.get(sighting_id)
    sighting = database[sighting_id]
    return render_template("confirm_to_delete.template.html",
                           sighting=sighting)


@app.route('/delete-sighting/<sighting_id>', methods=["POST"])
def process_delete(sighting_id):
    sighting = database.get(sighting_id)
    del database[sighting_id]
    sightings.save(database)
    flash(f"Sighting titled {sighting['title']} has been deleted")
    return redirect(url_for("show_all_sightings"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
