from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/')
def home():
    if 'uuid' not in session:
        return redirect('/login_page')
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/login_page')
    context = {
        "user" : User.get_one(session['uuid'])
    }
    return render_template('dashboard.html', **context)

@app.route('/login_page')
def login():
    return render_template('login_page.html')

@app.route('/register')
def register():
    return render_template('register_page.html')

@app.route('/dishes')
def dishes():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('dishes.html')

@app.route('/dishes/<int:id>')
def dish_id(id):
    if 'uuid' not in session:
        return redirect('/')
    context = {
            "id" : id
        }
    return render_template('dishes.html', **context)

@app.route('/create_recipe')
def create_dish():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('create_recipe.html')

@app.route('/recipe_page')
def recipe_page():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('recipe_page.html')

@app.route('/family_page')
def family_page():
    if 'uuid' not in session:
        return redirect('/')
        
    recipes = len(User.get_users_recipes('uuid'))

    context = {
        'user' : User.get_one(session['uuid']),
        'all_fam' : User.get_users_families('uuid'),
        'recipes' : recipes
    }
    return render_template('family_page.html', **context)

@app.route('/create_fam')
def create_fam():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('create_fam.html')

@app.route('/user/edit')
def edit_user():
    if 'uuid' not in session:   
        return redirect('/login')
    context = {
        "user" : User.get_one(session['uuid'])
    }
    return render_template('edit_user.html', **context)

@app.route('/family/edit')
def edit_family():
#create a validation that someone has the ability to edit a family page
    return render_template('edit_user.html')