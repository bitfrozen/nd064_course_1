from flask import Flask, render_template
from model import db
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("welcome.html",
                           message="Message from variable")


@app.route("/records")
def record_view():
    record = db[0]
    return render_template("record.html", record=record)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
