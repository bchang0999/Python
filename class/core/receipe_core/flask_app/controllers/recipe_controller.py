from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe



#Route to new Recipe
@app.route("/add_new_recipe")
def route_to_new_recipe():
    if 'user_id' not in session:
        flash("please log in before proceeding")
        return redirect("/")
    return render_template("add_new_recipe.html")



@app.route("/recipe_delete/<int:id>")
def delete(id):
    data={"id":id}
    Recipe.delete(data)
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard_recipe():
    recipes = Recipe.display_all_recipes() 
    print (recipes)
    return render_template("dashboard.html", recipe = recipes)

#CREATEEEEEE
@app.route('/new_recipe', methods =["POST"])
def create_recipe():
    if len (request.form ["recipe_name"]) <1:
        flash("please fill out name")
        return redirect("/add_new_recipe")
    if len (request.form ["description"]) <1:
        flash("please fill out description")
        return redirect("/add_new_recipe")
    if len (request.form ["instructions"]) <1:
        flash("please add instructions")
        return redirect("/add_new_recipe")
    if len (request.form ["under_thirty"]) <1:
        flash("please select yes/no")
        return redirect("/add_new_recipe")    
    if len (request.form ["created_at"]) <1:
        flash("please select date")
        return redirect("/add_new_recipe")
    data={
        'recipe_name':request.form ['recipe_name'],
        'description':request.form ['description'],
        'instructions':request.form ['instructions'],
        'under_thirty':request.form ['under_thirty'],
        'created_at':request.form ['created_at'],
        'user_id' :session['user_id']
    }
    Recipe.create(data)
    return redirect("/dashboard")






#updateeeeee link
@app.route('/recipes/edit/<int:id>')
def update(id):
    data = {
        "id" : id
    }
    one_recipe = Recipe.view_one_recipe(data)
    return render_template("recipes_edit.html", one_recipe = one_recipe, id=id)

#update action
@app.route('/updating...', methods = ['POST'])
def updated():
    if len (request.form ["created_at"]) <1:
        flash("please fill out date")
        return redirect(f"/recipes/edit/{request.form ['id']}")
    if len (request.form ["recipe_name"]) <1:
        flash("please fill out name")
        return redirect(f"/recipes/edit/{request.form ['id']}")
    if len (request.form ["description"]) <1:
        flash("please fill out description")
        return redirect(f"/recipes/edit/{request.form ['id']}")
    if len (request.form ["under_thirty"]) <1:
        flash("please select yes or no")
        return redirect(f"/recipes/edit/{request.form ['id']}")
    data = {
        'id':request.form ['id'],
        'recipe_name':request.form ['recipe_name'],
        'description':request.form ['description'],
        'instructions':request.form ['instructions'],
        'created_at' :request.form ['created_at'],
        'under_thirty':request.form ['under_thirty'],
        
    }
    Recipe.update(data)
    return redirect("/dashboard")


#view istructions route
@app.route('/recipes/<int:id>')
def view(id):
    data = {
        "id" : id
    }
    query_data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(query_data)
    recipes = Recipe.view_one_recipe(data) 
    one_recipe = Recipe.view_one_recipe(data)
    return render_template("view.html", user = user, recipe = recipes, one_recipe = one_recipe, id=id)
