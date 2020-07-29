# Form Processing

Create the following routes:

# GET / 

Display a text-box which the user will enter the number 1, 2 or 3. There is no need to check if the user enters a wrong number.

# POST /

In the POST version of the above, display the `1.jpg` in the template if the user entered a `1` previously, `2.jpg` if the user has entered a `2` previously, and so on and so forth.

# GET /contact-us

Display the form shown in `form.template.html`

# POST /contact-us

Extract out the name, gender, whether we can contact the user, comments and whether the user has accepted the terms and conditions. 
Display out the user's input in an unordered list.

# Possible Solutions for Part 1

## METHOD 1:
```
@app.route('/', methods=["POST"])
def process_number():
    number = int(request.form.get('number'))
    image = ""
    if number == 1:
        image="1.jpg"
    if number == 2:
        image="2.jpg"
    if number == 3:
        image="3.jpg"
    return render_template('show_number_pic.template.html', image=image)
```

## METHOD 2:
```
@app.route('/', methods=["POST"])
def process_number():
    number = int(request.form.get('number'))
    return render_template('show_number_pic.template.html', number=number)
```

```
<body>
	{% if number == 1 %}
	<img src="/static/1.jpg"/>
    {% elif number == 2 %}
	<img src="/static/2.jpg"/>
    {% elif number == 3 %}
	<img src="/static/3.jpg"/>
    {% else %}
    <p>Invalid number</p>
    {% endif %}
</body>
```

## Method 3
Please see the answer