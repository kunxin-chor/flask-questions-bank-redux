from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
import sightings


app = Flask(__name__)

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

    sighting = sightings.create_sighting(next_id)

    database[next_id] = sighting
    sightings.save(database)

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

    sighting = sightings.create_sighting(sighting_id)

    database[sighting_id] = sighting

    sightings.save(database)

    return redirect(url_for("show_all_sightings"))


@app.route('/delete-sighting/<sighting_id>')
def show_delete_confirmation(sighting_id):
    # sighting = database.get(sighting_id)
    sighting = database[sighting_id]
    return render_template("confirm_to_delete.template.html",
                           sighting=sighting)


@app.route('/delete-sighting/<sighting_id>', methods=["POST"])
def process_delete(sighting_id):
    del database[sighting_id]
    sightings.save()
    return redirect(url_for("show_all_sightings"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
