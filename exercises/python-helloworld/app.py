from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db
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


@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    if request.method == "POST":
        card = {"name": request.form['name'],
                "surname": request.form['surname']}
        db.append(card)
        save_db()
        return redirect(url_for('record_view', index=len(db) - 1))
    else:
        return render_template("add_record.html")


@app.route("/delete_record/<int:index>", methods=["GET", "POST"])
def delete_record(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('hello'))
        else:
            return render_template('delete_record.html', record=db[index])
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
