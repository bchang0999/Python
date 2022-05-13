from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.hobby = data["hobby"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('practice_one').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO Users ( first_name , last_name ,hobby , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(hobby)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        results= connectToMySQL('practice_one').query_db( query, data )
        return results