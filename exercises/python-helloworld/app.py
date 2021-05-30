from flask import Flask, render_template, abort
from model import db
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("welcome.html",
                           records=db)


@app.route("/record/<int:index>")
def record_view(index):
    try:
        record = db[index]
        return render_template("record.html",
                               record=record,
                               index=index,
                               max_index=len(db) - 1)
    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
