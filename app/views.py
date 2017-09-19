from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    ###if request.method == 'POST':
     ###   if request.form['username'] != app.config['USERNAME']:
      ###      error = 'Invalid username'
      ###  elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
      ###  else:
       ###     session['logged_in'] = True
       ###     flash('You were logged in')
        ###    return redirect(url_for('/'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('/'))

@app.route('/register')
def register():
    return render_template("register.html")