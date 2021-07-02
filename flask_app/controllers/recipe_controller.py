from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/recipe/create', methods =['POST'])
def create_recipe():
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        return redirect('/create_dish.html')
    info = {
        **request.form
    }
    Recipe.new_recipe(info)
    return redirect('/recipe_page.html')

@app.route('/recipe/update', methods=['POST'])
def update_recipe():
    return redirect('/dishs.html')