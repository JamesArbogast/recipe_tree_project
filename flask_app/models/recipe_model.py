from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.user_model import User

DATABASE = 'recipe_tree_db'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.ingredient_list = data['ingredient_list']
        self.directions = data['directions']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

#C
    @classmethod
    def new_recipe(cls, info):
        query = 'INSERT INTO recipes (recipe_name, ingredient_list, directions, description) VALUES (%()s,%()s,%()s'


#R


#U



#D