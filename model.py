from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
<<<<<<< HEAD
   
    
=======
    name = db.Column(db.String, unique=True)
    phone = db.Column(db.Integer, unique=True)

>>>>>>> 6f44713361a01aeb46341165a601786aac42bca6
class FAQ(db.Model):
    NO = db.Column(db.Integer, primary_key=True)
    Questions = db.Column(db.String)
    Answers = db.Column(db.String)    