#this is where the code starts
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import app


class Recipe:
    db="recipes"
    def __init__(self,data):
        self.id = data["id"]
        self.recipe_name = data["recipe_name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under_thirty = data["under_thirty"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]



    @classmethod
    def display_all_recipes(cls):
        query="SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)

        recipe = []

        for one_recipe in results:
            recipe.append(cls(one_recipe))

        return recipe

#CREATEEEEEEEE
    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes (recipe_name, description, instructions, under_thirty,created_at, updated_at, user_id) VALUES (%(recipe_name)s, %(description)s,%(instructions)s, %(under_thirty)s, %(created_at)s, NOW(), %(user_id)s);"

        results = connectToMySQL('recipes').query_db(query, data)

        return results


#READDDDDDDDDDDDDDDDDDDDDDDDDD
    @classmethod
    def view_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])




#Updateeeeeeeee
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET recipe_name = %(recipe_name)s, description = %(description)s, instructions = %(instructions)s, under_thirty = %(under_thirty)s,created_at = %(created_at)s WHERE id = %(id)s;"
        connectToMySQL('recipes').query_db(query, data)







#Deleteeeeeeeee
    @classmethod
    def delete(cls, data):
        query="DELETE FROM recipes WHERE id = %(id)s"
        results = connectToMySQL('recipes').query_db(query, data)

