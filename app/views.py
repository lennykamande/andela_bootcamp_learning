import os
from flask import Flask, url_for,render_template, request, flash, redirect, session
from app import app
from models import User, Shoppinglist

@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        res = User.login(username=username, password=password)
        print(res)
        if res == True:
            return redirect(url_for('dashboard'))
    else:
        
        return render_template('login.html')

@app.route('/dashboard')
def dashboard_view():
    """route to render dashboard page"""
    return render_template('dashboard.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
    # counter check if password is the same
        password = request.form['password']
        confpassword = request.form['confpassword']

        if password != confpassword:
            
            return redirect(url_for('register'))
        res = User.signup(username, email, password)
        if res == "username or email exists":
            flash('username or email already taken', 'alert-danger')
            return redirect(url_for('signup'))
    else:    
        return render_template('register.html')
