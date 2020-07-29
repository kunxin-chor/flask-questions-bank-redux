from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def ask_for_number():
    return render_template('get_number_form.template.html')


@app.route('/', methods=["POST"])
def process_number():
    number = int(request.form.get('number'))
    return render_template('show_number_pic.template.html', number=number)


@app.route('/contact-us')
def show_contact_form():
    return render_template('form.template.html')


@app.route('/contact-us', methods=["POST"])
def process_contact_form():
    if 'democheckbox' in request.form:
        accept = True
    else:
        accept = False

    name = request.form.get('name')
    gender = request.form.get('sex')
    comment = request.form.get('comment')
    can_contact = True if request.form.get('can-contact') == "yes" else False

    # alternate method:
    # accept = request.form.get('democheckbox')
    # if accept == 'yes':
    #     accept = True
    # else:
    #     accept = False

    return render_template('display_results.template.html', context={
        "name": name,
        "gender": gender,
        "comment": comment,
        "can_contact": can_contact,
        "accept": accept
    })


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
