from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request
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
        query = 'INSERT INTO recipes (recipe_name, ingredient_list, directions, description, spice_level, genre, users_id) VALUES (%(recipe_name)s, %(ingredient_list)s, %(directions)s, %(description)s, %(spice_level)s, %(genre)s, %(users_id)s);'
        data = {
            "recipe_name" : info['recipe_name'],
            "ingredient_list" : info['ingredient_list'],
            "directions" : info['directions'],
            "description" : info['description'],
            "spice_level" : info['spice_level'],
            "genre" : info['genre'],
            "users_id" : info['users_id']
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
        return results

    @classmethod
    def get_recipe(cls,id):
        query = "SELECT * FROM recipes where id = %(id)a;"
        data = {
            "id" : id
        }
        return connectToMySQL(DATABASE).query_db(query, data)

#U
    @classmethod
    def update_recipe(cls, info):
        query = "INSERT INTO recipes SET (recipe_name = %(recipe_name)s, ingredient_list = %(ingredient_list)s, directions = %(directions)s, description = %(description)s, spice_level = %(spice_level)s, genre = %(genre)s, user_id = %(users_id)s);" 
        data = {
            "recipe_name" : info['recipe_name'],
            "ingredient_list" : info['ingredient_list'],
            "directions" : info['directions'],
            "description" : info['description'],
            "spice_level" : info['spice_level'],
            "genre" : info['genre'],
            "users_id" : info['users_id']
        }
        return connectToMySQL(DATABASE).query_db(query, data) 

#D

    @classmethod
    def delete_recipe(cls, id):
        query = "DELETE FROM recipes WHERE ID = %(id)s;"
        data = {
            "id" : id
        }
        connectToMySQL(DATABASE).query_db(query, data)
        return print(f"The recipe with ID: {id} has been permanently removed!")

#D

    @staticmethod
    def validate_user(recipe):
        is_valid = True # we assume this is true
        if len(recipe['recipe_name']) < 4:
            flash("Recipe name should be more than 4 characters")
            is_valid = False
        if len(recipe['directions']) < 60:
            flash("Directions should have a minimum of 60 characters!")
            is_valid = False
        if len(recipe['description']) < 25:
            flash("Description needs to be at least 25 characters!")
            is_valid = False
        if len(recipe['spice_level']) < 0:
            flash("Use a proper spice level!")
            is_valid = False
        if len(recipe['genre']) < 3:
            flash("genre must be at least 3 characters")
            is_valid = False
        return is_valid
