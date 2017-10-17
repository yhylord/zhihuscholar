from flask import session, render_template, redirect, url_for
from flask_login import login_user
from zhihuscholar import app, bcrypt, login_manager
from .forms import LoginForm
from .models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        registered_user = User.query.filter_by(email=email).first()
        if registered_user:
            password_hash = registered_user.password
            password = form.password.data
            if bcrypt.check_password_hash(password_hash, password):
                login_user(registered_user)
                session['remember_me'] = form.remember_me.data
                return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run()
