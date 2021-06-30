from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import app
import re

DATABASE_SCHEMA = 'recipe_tree_db'

class Family: #pascal case -> first upper, rest lower, word is singular
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['family_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#C
    @classmethod
    def create(cls, info):
        query = "INSERT INTO families (family_name) VALUES (%(family_name)s)"
        data = {
            "family_name" : info['family_name'],
        }
        new_family_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return new_family_id

#R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM families"
        all_table_name = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        all_families = []
        for family in all_table_name:
            all_families.append(cls(family))
        return all_table_name

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM families WHERE id= %(family_id)s;"
        data = {
            "family_id": id
        }
        print(data)
        one_table_name = connectToMySQL(DATABASE_SCHEMA).query_db(query, data) 
        print(one_table_name)
        return one_table_name

    @classmethod
    def get_one_by_name(cls, family_name):
        query = "SELECT * FROM families WHERE name= %(family_name)s;"
        data = {
            "family_name": family_name
        }
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return result

    @classmethod
    def get_families_users(cls, id):
        query = "SELECT family_name FROM families JOIN users_has_families ON users_has_families.family_id = families.id JOIN users ON users_has_families.user_id = users.id WHERE users.id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return result

    @classmethod
    def get_families_recipes(cls, id):
        query = "SELECT recipe_name FROM recipes JOIN users ON users.id = user_id WHERE users.id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return result
    
#U
    @classmethod
    def update_one(cls, info):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, pw=%(pw)s WHERE id=%(id)s;"
        data = {
            "first_name": info['first_name'],
            "last_name": info['last_name'],
            "email": info['email'],
            "pw": info['pw'],
            "id": info['id']
        }
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return result
#D
    @classmethod
    def delete_one(cls, id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        data = {
            "id": id
        }
        connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        print(f"The user with the ID:{id} has been deleted")
        return id