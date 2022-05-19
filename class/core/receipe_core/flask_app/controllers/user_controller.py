from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/")
def index():
    return render_template("index.html")




#VALIDATE REGISTER ROUTE
@app.route("/register", methods=["POST"])
def register():
    # Step1 Validate information
    if not User.validate_register(request.form):
        return redirect("/")

    #step2 Collect Data for query
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" :pw_hash
    }

    #step3 run query (add user to data)
    new_user_id = User.register_user(query_data)
    #step 4 log them in via session
    session['user_id'] = new_user_id

    #step5 redirect elsewhere
    return redirect("/dashboard")

    #LOGIN ROUTE

@app.route("/login", methods=["POST"])
def login():
    #1 Validate our login info
    if not User.validate_login(request.form):
        return redirect("/")
    #2pull users from data to log them in 
    logged_user = User.get_by_email(request.form)
    session['user_id'] = logged_user.id

    #3 redirect eslsewhere
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        flash("please log in before proceeding")
        return redirect("/")
    query_data = {
        "user_id": session["user_id"]
    }    
    user = User.get_by_id(query_data)
    recipes = Recipe.display_all_recipes()
    
    return render_template("dashboard.html", user = user, recipe = recipes)




@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


