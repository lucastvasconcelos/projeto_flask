from app import app,db,login_manager
from flask import render_template,flash,redirect,url_for
from flask_login import login_user,logout_user
from app.models.forms import LoginForm
from app.models.tables import User

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        user_exist = User.query.filter_by(username=form.username.data).first()
        if user_exist and user_exist.password == form.password.data:
            login_user(user_exist)
            flash('Logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login')
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))