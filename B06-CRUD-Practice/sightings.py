import json


def create_sighting(next_id, request):
    sighting = {
        "id": next_id,
        "title": request.form.get('title'),
        "email": request.form.get("email"),
        "shape_category": request.form.get("shape-category"),
        "other-shape": request.form.get('other-shape'),
        "lat": request.form.get("lat"),
        "lng": request.form.get("lng"),
        "description": request.form.get('comments')
    }
    return sighting


def save(database):
    with open("db.json", "w") as fileptr:
        json.dump(database, fileptr)


def load():
    database = {}
    with open("db.json", "r") as fileptr:
        database = json.load(fileptr)
    return database


def get_by_id(database, sighting_id):
    return database.get(sighting_id)
