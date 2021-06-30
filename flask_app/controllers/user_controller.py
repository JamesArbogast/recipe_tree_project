from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/create', methods = ['POST'])
def user_create():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect('/register')
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    info = {
        **request.form,
        "hash_pw" : hash_pw
    }   
    user_id = User.create(info)
    session['uuid'] = user_id
    print(session['uuid'])
    return redirect('/')

@app.route('/user/edit')
def edit_user():
    if 'uuid' not in session:   
        return redirect('/login')
    context = {
        "user" : User.get_one(session['uuid'])
    }
    return render_template('edit_user.html', **context)

@app.route('/user/update', methods=['POST'])
def update_user():
    user = User.get_one(session['uuid'])
    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "pw": user['pw'],
        "id": session['uuid']
    }
    User.update_one(info)
    return redirect('/')

@app.route('/user/delete', methods=['POST'])
def delete_user():
    User.delete_one(session['uuid'])
    session.clear()
    return redirect('/')