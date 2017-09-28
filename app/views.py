import os
from flask import Flask, url_for,render_template, request, flash, redirect, session
from app import app
from models import User, Shoppinglist

test = User()
shop = Shoppinglist()
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res = test.login(email, password)
        if res is True:
            session['logged_in'] = True
            session['email'] = email
            print session['email']
            return redirect('/dashboard')
    else:
        
        return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard_view():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        items = shop.view_lists(owner=session["email"])
        print(items, "items")
        return render_template('dashboard.html', data = items)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['pass']
        confpassword = request.form['passc']
        if password != confpassword:
            return redirect(url_for('register'))
        res = test.signup(username, email, password)
        if res == "username or email exists":
            flash('username or email already taken', 'alert-danger')
            return redirect(url_for('register'))
        else:
            return redirect(url_for('login'))
    else:    
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/add_item', methods=['GET','POST'])
def add_item():
    error = None
    if request.method=='POST':
        name = request.form['name']
        description = request.form['description']
        owner = session["email"]
        if not name.strip() and description.strip():
            return redirect(url_for('add_item', error="No Data given"))
        else:
            result = shop.newlist(name, description, owner)
            print(result, ">>>>>>>>")
            if result == 'success':
                return redirect(url_for('dashboard_view')) 
        
    else:    
        return render_template('add-item.html')
