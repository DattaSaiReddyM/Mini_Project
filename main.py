from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return  render_template('dashboard.html')

@app.route("/login")
def login():
    return  render_template('login.html')

@app.route("/signup")
def signup():
    return  render_template('signup.html')

@app.route("/profile")
def profile():
    return  render_template('profile.html')

@app.route("/faq")
def faq():
    return  render_template('faq.html')

@app.route("/forms",methods=["GET","POST"])
def forms():
    if request.method == 'GET':
        return  render_template('Forms.html')
    if request.method == 'POST':
        print(request.form['fname'])
        
        return  "THIS IS POST REQUEST"


if __name__=="__main__":
    app.run(debug=True)