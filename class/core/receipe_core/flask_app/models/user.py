#this is where the code starts
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import app
from flask import flash

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

class User:
    db="recipes"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_night = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def validate_register(form_data):
        is_valid = True
        if len(form_data["first_name"]) < 1:
            flash("First name must be present")
            is_valid = False
        if len(form_data["last_name"]) < 1:
            flash("Last name must be present")
            is_valid = False
        if len(form_data["email"]) < 1:
            flash("Email must be present")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid Email")
            is_valid = False

        if len(form_data["password"]) < 7:
            flash("Password must be at leasst 7 characters long!")
            is_valid = False
        if form_data["password"] != form_data["conf_password"]:
            flash("Password and Confirmation Password dont match!")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True
        user_in_db = User.get_by_email(form_data)
        # user is not registered in the db
        if not user_in_db:
            flash("Invalid Email/Password")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, form_data['password']):
            flash("Invalid Email/Password")
            is_valid = False
        return is_valid

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        results = connectToMySQL("recipes").query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s"
        result = connectToMySQL("recipes").query_db(query,data)

        if len(result) < 1:
            return False
        return cls(result[0])


