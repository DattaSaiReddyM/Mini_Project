from flask import Flask, render_template, request, redirect, url_for
from model import *
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(os.path.abspath(os.path.dirname(__file__)),"database.sqlite3")
db.init_app(app)
with app.app_context():
    print("database created")
    db.create_all()


@app.route("/")
def home():
    users =  User.query.all()
    return  render_template('dashboard.html')

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return  render_template('login.html')
    if request.method == 'POST':
        email = request.form["email"]
        faq =  User.query.filter_by(email = email).first()
        print(faq.email)
        return redirect(url_for('home'))
        
    

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'GET':
        return  render_template('signup.html')
    if request.method == 'POST':
        faq = User(
            email=request.form["email"],
            password=request.form["password"],
        )
        db.session.add(faq)
        db.session.commit()
        return redirect(url_for('login'))
   

@app.route("/profile")
def profile():
    return  render_template('profile.html')

@app.route("/faq",methods=["GET","POST"])
def faq():
    if request.method == 'GET':
        
        faq = FAQ.query.all()
    
    
        return  render_template('faq.html',faq=faq)
    
@app.route("/crop", methods=["GET"]) 
def crop():
    return render_template('Crop.html')

@app.route("/forms",methods=["GET","POST"])
def forms():
    if request.method == 'GET':
        return  render_template('Forms.html')
    if request.method == 'POST':
        print(request.form['fname'])
        
        return  "THIS IS POST REQUEST"


if __name__=="__main__":
    app.run(debug=True)