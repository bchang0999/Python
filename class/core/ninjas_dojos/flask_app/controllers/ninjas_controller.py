from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



#Route to ninja page
@app.route("/ninja")
def route_ninja():
    dojos=Dojo.display_all_dojos()
    return render_template("ninjas.html", dojos= dojos)


@app.route("/ninja_process", methods = ["POST"])
def process():
    data={
        'dojo_id':request.form ['Dojo'],
        'first_name':request.form ['first_name'],
        'last_name':request.form ['last_name'],
        'age':request.form ['age'],
    }
    Ninja.create_ninja(data)
    return redirect("/dojos")
