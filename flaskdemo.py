import flask
import csv
import json

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello <b>World</b><font color='red'>!</font>"

@app.route("/json")
def jsonurl():
    with open("mesures.csv") as f:
        reader = csv.DictReader(f)
        diff = [abs(float(row["VM"]) - float(row["VT"])) for row in reader]
        return json.dumps(diff)

app.run()

