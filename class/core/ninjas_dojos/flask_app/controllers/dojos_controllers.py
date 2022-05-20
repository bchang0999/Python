from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja 


@app.route("/dojos")
def index():
    dojo = Dojo.display_all_dojos()
    print (dojo)
    return render_template("home.html", dojo = dojo)

#create New Dojo
@app.route("/dojos_create", methods =["POST"])
def create_dojo():
    data={
        'name':request.form ['name'],
    }
    Dojo.create_dojo(data)
    return redirect("/dojos")


#route to read what ninjas are inside what dojo
@app.route('/dojos/<int:id>')
def update(id):
    data = {
        "id" : id
    }
    
    dojo = Dojo.students(data)
    return render_template("dojos.html",id=id, dojo = dojo)




