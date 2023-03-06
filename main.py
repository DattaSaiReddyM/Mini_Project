from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return  render_template('home.html')

@app.route("/login")
def login():
    return  render_template('Login.html')

@app.route("/forms",methods=["GET","POST"])
def forms():
    if request.method == 'GET':
        return  render_template('Forms.html')
    if request.method == 'POST':
        print(request.form['fname'])
        
        return  "THIS IS POST REQUEST"


if __name__=="__main__":
    app.run()