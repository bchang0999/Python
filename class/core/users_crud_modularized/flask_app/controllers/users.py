from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

#display users/home page
@app.route('/')
def display():
    users=User.display_all() 
    return render_template("all_users.html", users= users)



#create user page
@app.route("/new_user", methods=["POST"])
def new_user_page():

    return render_template("new_user.html")


#new user datat into sql
@app.route("/new_user_insert", methods=["POST"])
def insert():
    data = {
        'first_name':request.form ['first_name'],
        'last_name':request.form ['last_name'],
        'email':request.form ['email'],
        }

    user_id = User.add_user(data)
    return redirect(f"/new_user_display/{user_id}")

#display new user PAGE!
@app.route("/new_user_display/<int:id>")
def display_user(id):
    data={"id":id}
    user_display_variable = User.user_display(data)
    return render_template("display_user.html",user_display_variable=user_display_variable)

#display update PAGE!
@app.route("/user_update/<int:id>")
def display_update_form(id):
    data={"id":id}
    user = User.user_display_pars(data)
    return render_template("update_user.html", user=user)

@app.route("/user_update_action", methods = ["POST"])
def hard_update():
    data = {
        'id' :request.form ['id'],
        'first_name':request.form ['first_name'],
        'last_name':request.form ['last_name'],
        'email':request.form ['email'],
        }
    User.user_update(data)
    return redirect("/")

@app.route("/user_delte/<int:id>")
def delete(id):
    data={"id":id}
    User.delete(data)
    return redirect("/")