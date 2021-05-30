import json


def load_db():
    with open("records_db.json") as f:
        return json.load(f)


db = load_db()
