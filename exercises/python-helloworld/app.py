from flask import Flask, render_template, abort, jsonify
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


@app.route("/api/record/")
def api_record_list():
    return jsonify(db)


@app.route("/api/record/<int:index>")
def api_record_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
