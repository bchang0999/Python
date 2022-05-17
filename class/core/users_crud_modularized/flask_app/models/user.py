from ast import Return
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #dispay all users initially
    @classmethod
    def display_all(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL('user_crud_module').query_db(query)

        users = []

        for one_user in results:
            users.append(cls(one_user))

        return users

    #create
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s,%(email)s, NOW(), NOW());"

        results = connectToMySQL('user_crud_module').query_db(query, data)

        return results
        
        
    #read
    @classmethod
    def user_display(cls, data):
        query="SELECT * FROM users WHERE id = %(id)s"
        return connectToMySQL('user_crud_module').query_db(query, data)

        



    #update
    @classmethod
    def user_update(cls, data):
        query="UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return connectToMySQL('user_crud_module').query_db(query, data)

        
    #user display pars
    @classmethod
    def user_display_pars(cls, data):
        query="SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('user_crud_module').query_db(query, data)
        
        return cls (results [0])

    @classmethod
    def delete(cls, data):
        query="DELETE FROM users WHERE id = %(id)s"
        results = connectToMySQL('user_crud_module').query_db(query, data)