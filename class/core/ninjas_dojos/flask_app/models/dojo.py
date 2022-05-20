from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import ninja

class Dojo:
    db="Dojos_Ninjas"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninja=[]

#CREATE
    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        results = connectToMySQL(cls.db).query_db(query, data)

        return results


#READ
    @classmethod
    def view_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

#READ ALL
    @classmethod
    def display_all_dojos(cls):
        query="SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)

        dojo = []

        for one_dojo in results:
            dojo.append(cls(one_dojo))
        
        return dojo

#Left Join ---- Dojos with their Ninjas
    @classmethod
    def students(cls, data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)

        dojo = cls( results[0])

        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "dojo_id" : row["dojo_id"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.ninja.append( ninja.Ninja( ninja_data ))
        return dojo