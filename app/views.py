"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import db, app
from .forms import myform 
from models import User
from random import randint
from app import app
from flask import render_template, request, redirect, url_for,flash,jsonify
from werkzeug import secure_filename
from sqlalchemy.sql import functions

import os
import random
import json


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
    
@app.route('/profile/', methods =('GET','POST'))
def profile():
    form =  myform()
    userid = random.randint(62000000, 620099999)
    print 'test'
    if request.method == 'POST': #and form.validate_on_submit():
        print 'validate'
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        sex = request.form['sex']
        file = request.files['image']
        image = secure_filename(file.filename)
        file.save(os.path.join("picture", image))
        user = User(userid, image, firstname, lastname, age, sex)
        db.session.add(user)
        db.session.commit()
        flash('File Upload Complete!!!')
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form)

@app.route('/profiles/', methods =['GET','POST'])
def profiles():
    profiles = User.query.all()
    storage = []
    if request.method == 'POST': #or request.headers['Content-Type'] == 'application/json':
        for users in profiles:
            storage.append({'userid':users.userid, 'image':users.image, 'first name':users.firstname,'last name':users.lastname,'age':users.age,'sex':users.sex})
        users ={'users':storage}
        return jsonify(users)
    else:
        return render_template('profiles.html',profiles=profiles)
        
#@app.route('/profile/userid/', methods=['POST','GET'])



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
