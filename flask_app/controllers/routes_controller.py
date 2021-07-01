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
        return redirect('/')
    render_template('dashboard.html')

@app.route('/login_page')
def login():
    return render_template('login_page.html')

@app.route('/register_page')
def register():
    return render_template('register_page.html')


@app.route('/dishes/<int:id>')
def dish_id(id):
    if 'uuid' not in session:
        return redirect('/')
    context = {
            "id" : id
        }
    return render_template('dishes.html', **context)

@app.route('/create_dish')
def create_dish():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('create_dish.html')

@app.route('/recipe_page')
def recipe_page():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('recipe_page.html')

@app.route('/family_page')
def family_page():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('family_page.html')

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