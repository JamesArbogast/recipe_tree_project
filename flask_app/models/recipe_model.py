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
        self.spice_level = data['spice_level']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

#C
    @classmethod
    def new_recipe(cls, info):
        query = "INSERT INTO recipes (recipe_name, ingredient_list, directions, description, spice_level, genre, user_id) VALUES ('%()s', '%()s','%()s, %()s','%()s', %()s , '%()s', %()s);"

        data = {
            "recipe_name" : info['recipe_name'],
            "ingredient_list" : info['ingredient_list'],
            "directions" : info['directions'],
            "description" : info['description'],
            "spice_level" : info['spice_level'],
            "genre" : info['genre'],
            "user_id" : info['user_id']
        }
        return connectToMySQL(DATABASE).query_db(query, data)

#R
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for one_recipe in results:
            recipes.append(cls(one_recipe))
            return recipes

    @classmethod
    def get_recipe(cls, id):
        query = "SELECT * FROM recipe where id = %(id)s"

        data = {
            'recipe_id' : id
        }
        return connectToMySQL(DATABASE).query_db(query, data)

#U
    @classmethod
    def update_recipe(cls, info):
        query = "UPDATE recipes set recipe_name = %(recipe_name)s, ingredient_list = %(ingredient_list)s, directions = %(directions)s, description = %(description)s, spice_level = %(spice_level)s, genre = %(genre)s, user_id = %(user_id)s"

        data = {
            "recipe_name" : info['recipe_name'],
            "ingredient_list" : info['ingredient_list'],
            "directions" : info['directions'],
            "description" : info['description'],
            "spice_level" : info['spice_level'],
            "genre" : info['genre'],
            "user_id" : info['user_id']
        }
        return connectToMySQL(DATABASE).query_db(query, data)


#D

    @classmethod
    def delete_recipe(cls, id):
        query = 'Delete from recipes where id = %(id)s'
        data = {
            'id' : id
        }
        connectToMySQL(DATABASE).query_db(query, data)
        return id
