from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.full_name = data["full_name"]
        self.Email = data["Email"]
        self.create_on = data["create_On"]
        self.Last_Updated_On = data["Last_Updated_On"]

#read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_crud').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users



#create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO Users ( full_name ,Email , create_on, Last_Updated_On ) VALUES ( %(full_name)s , %(Email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        results= connectToMySQL('users_crud').query_db( query, data )
        return results

#update
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET full_name = %(full_name)s, Email = %(Email)s, Last_Updated_On = %(Last_Updated_On)s WHERE id= %(id)s; "
        connectToMySQL('users_crud').query_db( query, data )


#delete
    @classmethod
    def delete(cls,data):
        query= "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('users_crud').query_db( query, data )
