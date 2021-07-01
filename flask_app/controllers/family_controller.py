from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.family_model import Family
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/family/create', methods = ['POST'])
def family_create():
    is_valid = Family.validate_family(request.form)
    if not is_valid:
        return redirect('/register')
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    info = {
        **request.form,
        "hash_pw" : hash_pw
    }   
    user_id = Family.create(info)
    session['uuid'] = user_id
    print(session['uuid'])
    return redirect('/')

@app.route('/family/update', methods=['POST'])
def update_user():
    user = Family.get_one(session['uuid'])
    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "pw": user['pw'],
        "id": session['uuid']
    }
    Family.update_family(info)
    return redirect('/')

@app.route('/user/delete', methods=['POST'])
def delete_user():
    Family.delete_one(session['uuid'])
    session.clear() 
    return redirect('/')

@staticmethod
def validate_family(family):
    is_valid = True
    if len(family['family_name']) < 2:
        flash("First name must be at least 2 characters.")
        is_valid = False 
    return is_valid
