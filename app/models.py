from . import db

class User (db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True)
    fname = db.Column(db.String(15), unique = True)
    lname = db.Column(db.String(50), unique = True)
    age = db.Column(db.String(3), unique = True)
    sex = db.Column(db.String(10), unique = True)
    
    def _init_(self, fname,lname,sex,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex
        
    def _repr_(self):
        return '<User %r>' % self.username
        