from flask import render_template, flash, redirect, request, session, url_for, jsonify
from app import app, db, models

from forms import LoginForm, CreateForm

from app.utils.authentication import authenticate, get_user

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username')

    flash('Logged out')
    return redirect('index0')

@app.route('/', methods=['GET'])
@app.route('/index0', methods=['GET'])
def index0():
    return render_template("index.html", user = get_user(), message = "index0")

@app.route('/index1', methods=['GET'])
def index1():
    return render_template("index.html", user = get_user(), message = "index1")

@app.route('/index2', methods=['GET'])
def index2():
    return render_template("index.html", user = get_user(), message = "index2")

@app.route('/personalized_page', methods=['GET'])
@authenticate('user')
def personalized_page():
    return render_template('personal_page.html', user = get_user())


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data

        user = models.User.query.filter_by(username = session['username']).first()
        
        flash('Logged in')
        
        return redirect('index0')

    return render_template('login.html', login_form = login_form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = CreateForm()

    if create_form.validate_on_submit():
        new_user = models.User(fname = create_form.fname.data,
                               lname = create_form.lname.data,
                               nickname = create_form.nickname.data,
                               email = create_form.email.data,
                               username = create_form.username.data,
                               permissions = '')
        
        new_user.set_password(create_form.password.data)
        new_user.add_permission('user')
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('You have signed up!')
        return redirect('login')

    return render_template('create.html', create_form = create_form)


