from crypt import methods
from flask_app import app
from flask_app.models import user
from flask import render_template, session, request, redirect, flash

# CREATE


# READ
@app.route('/')
def reglog():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def registerUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'conf_password': request.form['conf_password']
    }

    user.User.createUser(data)

    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    if not user.User.login(data):
        return redirect('/')

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboardView():
    user_id = session['user_id']
    user_info = user.User.get_user_by_id(user_id)

    return render_template('dashboard.html', user_info=user_info)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
