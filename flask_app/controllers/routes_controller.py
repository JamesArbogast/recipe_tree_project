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
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    render_template('login_page.html')

@app.route('/register_page')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    render_template('register_page.html')

@app.route('/dishes')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    render_template('dishes.html')

@app.route('/create_dish')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    render_template('create_dish.html')

@app.route('/recipe_page')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    render_template('recipe_page.html')

