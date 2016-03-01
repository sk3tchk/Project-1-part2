from . import db

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(50))
    age = db.Column(db.String(3))
    sex = db.Column(db.String(10))
    
    def __init__(self, userid, image, firstname, lastname, age, sex):
        self.userid = userid
        self.image = image
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        
    def _repr_(self):
        return '<User %r>' % self.username
        