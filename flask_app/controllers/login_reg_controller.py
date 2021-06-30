from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/process_login', methods = ['POST'])
def process_login():
    list_of_users = User.get_one_by_email(request.form['email'])
    if len(list_of_users) <= 0:
        print("User doesn't exist")
        return redirect('/login')
    user = list_of_users[0]
    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        flash("Incorrect Password")
        return redirect('/login')
    session['uuid'] = user['id']
    return redirect('/')

@app.route('/logout')
def logout():
    if 'uuid' in session:
        session.clear()
    return redirect('/')