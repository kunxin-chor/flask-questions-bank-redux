# CRUD Practice

We will be using a **dictionary** as a database. Here are some reminders on how to use a dictionary

For all the examples below, assume that `db` is a dictionary.

```
db = {}
```

## Add to a dictionary

The generic syntax for adding a key to a dictionary which has a certain value is:
```
db['key'] = value
```

If the key is supposed to be a string, it must be enclosed in quotes. You can use **integers as keys as well**, don't be confused.

Or as a specific example, set the value `pi` to 3.14 in the `db` dictionary:

```
db['pi'] = 3.14
```

## Check if a key exists in a dictionary

```
if key in db: 
   print(db[key])
```

## Get a value by key
If you use 

```
v = db.get('pi')
```

v will be `None` if the key `pi` does not exist. If the key exists, then `v` will be the value of the key `pi`

## Remove a key
```
del db['key']
```

## You can store a dictionary as the value of a key
We can do the following:

```
employee = {
    "name":"Tan Ah Kow",
    "salary":3200
}

data[12] = emplyoee
```

With all these in mind, realise the following requirements:

* Create a global dictionary named `database`
* Create a route that display a form to allow the user to enter details about a UFO sighting. The details to capture are: title (string), date (string), time (string), email (string),
duration (int), latitude (float), longtitude (float) and description (textarea).
* Create a route that saves a new sighting. You need to find a way to create an unique id for each sighting and store it with each record.
* Create a route that displays all the title of sightings.
* The user should be able to select which sighting to view in details, delete or update
* Create the routes that allow the user to edit a sighting.
* Create the routes that allow the user to delete a sighting