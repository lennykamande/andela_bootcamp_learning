from flask import render_template, url_for, request, redirect

from app import app
from app.models import User, Shoppinglist
from flask_login import login_required, login_user, logout_user, login_manager


login_manager = LoginManager()


login_manager.init_app(app)
login_manager.login_message = "You must be Logged in to view this page"
login_manager.login_view = "login"


@app.route('/')
@login_required
def index():
    
    return render_template("dashboard.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        check = User.login(email,password)
        if (check == True):
            return redirect('/index')
    else:
        return("something fucked up")
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
           user = User.register(firstname,lastname, username, emailid, password) 
           return (url_for('/login'))
    else:
        return render_template("register.html")

