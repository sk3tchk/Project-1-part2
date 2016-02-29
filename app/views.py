"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import db, app
import json
import random
from random import randint
from app import app
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename
from sqlalchemy.sql import functions

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

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
    
@app.route('/profile/')
def profile():
    user = userForm()
    userid = random.randint(62000000,620099999)
    if request.method == 'POST' and form.validate_on_submit():
        firstname = request.form['fname']
        lastname = request.form['lname']
        age = request.form['age']
        sex = request.form['sex']
        file = request.form['image']
        image = secure_filename(file.filename)
        file.save(os.path.join("app/static/img", image))
        
        user = User(userid, fname, lname, sex, age, image)
        db.session.add(user)
        db.session.commit()
        flash('File Upload Complete!!!')
        return redirect(url_for('profile'))
    return render_template('forms.html', form = form)

@app.route('/profiles/', methods =['GET','POST'])
def profiles():
    profiles = User.query.all()
    storage = []
    if request.method == 'POST' or request.headers['Content-Type'] == 'application/json':
        for users in profiles:
            storage.append({'userid':users.userid, 'first name':users.fname,'last name':users.lname,'sex':users.sex,'age':users.age,'image':users.image})
        users ={'users':storage}
        return jsonify(users)
    else:
      return render_template('profiles.html',profiles=profiles)
        
@app.route('/profile/userid/', methods=['POST','GET'])



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
