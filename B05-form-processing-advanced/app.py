from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

appetizer_costs = {
    "appetizer-seafood": {
        "name": "Overprized chilled seafood",
        "price": 3.00,
        "image": "seafood.jpg"
    },
    "appetizer-fries": {
        "name": "Fries Sprinkled with Fake Truffle Powder",
        "price": 4.50,
        "image": "fries.jpg"
    },
    "appetizer-salad": {
        "name": "Minimal Effort Salad",
        "price": 6.00,
        "image": "salad.jpg"
    },
    "appetizer-fruit-salad": {
        "name": "Over-ripen fruit with unpeeled skin salad",
        "price": 5.00,
        "image": "fruits.jpg"
    }
}


@app.route('/')
def display_form():
    return render_template('form.template.html', appetizers=appetizer_costs)


@app.route('/', methods=["POST"])
def process_form():
    total_cost = 0
    appetizers = request.form.getlist('appetizers')
    for value in appetizers:
        total_cost += appetizer_costs[value]['price']

    seating = request.form.get('seating')
    if seating == "indoors-vip":
        total_cost += 10

    return f"Total Cost = {total_cost}"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
