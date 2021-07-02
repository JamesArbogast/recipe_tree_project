from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.family_model import Family
from flask_bcrypt import Bcrypt
import random

bcrypt = Bcrypt(app)

@app.route('/family/new', methods=['POST'])
def family_create():
    # is_valid = Family.validate_family(request.form['family_name'])
    # if not is_valid:
    #     return redirect('/login')
    # print(request.form['family_name'])
    info = {
        "family_name" : request.form['family_name'],
        "gen_id" : random.getrandbits(9)
        }
    family_id = Family.create(info)
    print(family_id)
    return redirect('/family_page')

@app.route('/family/update', methods=['POST'])
def update_family():
    user = Family.get_one(session['uuid'])
    info = {
        "family_name": request.form['family_name']
    }
    Family.update_family(info)
    return redirect('/')

@app.route('/family/delete', methods=['POST'])
def delete_family():
    Family.delete_one(session['uuid'])
    session.clear() 
    return redirect('/')