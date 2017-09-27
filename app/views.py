from flask import render_template, url_for, request, redirect, session

from app import app
from models import User, Shoppinglist



@app.route('/dashboard')
def dashboard():
    
    return render_template("dashboard.html")

@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        check = User(email,password)
        check.login
        if (check.login):
            return redirect(url_for('dashboard'))
    else:
       return render_template("login.html")
    

@app.route('/register',  methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        firstname=request.form['fname']
        lastname=request.form['lname']
        username=request.form['username']
        emailid=request.form['email']
        password = request.form['pass']
        cpassword = request.form['passc']
        if (password == cpassword):
           new_user = User(firstname,lastname, username, emailid, password) 
           new_user.register
           return redirect(url_for('login'))
    else:
        return render_template("register.html")

