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
    info = {
        "recipe_name": request.form['recipe_name'],
        "ingredient_list": request.form['ingredient_list'],
        "directions": request.form['directions'],
        "pw": request.form['description'],
        "id": request.form['spice_level']

    }
    Recipe.update_recipe(info)
    return redirect('/dishs.html')