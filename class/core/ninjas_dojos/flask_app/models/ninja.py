from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class Ninja:
    db="Dojos_Ninjas"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]




#CREATE
    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s,%(age)s, %(dojo_id)s);"

        results = connectToMySQL(cls.db).query_db(query, data)

        return results


#READ
    @classmethod
    def view_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

#READ ALL
    @classmethod
    def display_all_ninjas(cls):
        query="SELECT * FROM ninjas;"
        results = connectToMySQL(cls).query_db(query,)
        
        return results

