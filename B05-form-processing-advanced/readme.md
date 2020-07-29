# Advanced Form Processing

A pure HTML form is provided in `raw-form.html`

This form has some attributes missing that makes it not usable by Flask. Change this into a template, add the missing attributes that make its processable in Flask, then
display the form in a route.

Once the user has submitted the form, display all the choices the user has made, and the **total cost** of the booking.

## Possibel solution:

```
@app.route('/', methods=["POST"])
def process_form():
    total_cost = 0
    appetizers = request.form.getlist('appetizers')
    for value in appetizers:
        if value == "appetizer-seafood":
            total_cost += 3
        elif value == "appetizer-fries":
            total_cost += 4.5
        elif value == "appetizer-salad":
            total_cost += 6

    seating = request.form.get('seating')
    if seating == "indoors-vip":
        total_cost += 10

    return f"Total Cost = {total_cost}"
```