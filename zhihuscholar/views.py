from flask import jsonify, render_template, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from zhihuscholar import app, bcrypt, db, login_manager
from .forms import LoginForm, RegisterForm
from .models import Article, Feedback, User


@app.route('/')
@app.route('/index')
def index():
    articles = [Article.query.get(1)] # TODO replace placeholder
    return render_template('index.html', title='Home', articles=articles)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO Check for unique user
    # TODO Send confirmation email
    # TODO Add captcha
    form = RegisterForm()
    if form.validate_on_submit():
        password = form.password.data
        password_hash = bcrypt.generate_password_hash(password)
        new_user = User(name=form.name.data, email=form.email.data, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


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
                login_user(registered_user, remember=form.remember_me.data)
                return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/_update_feedback', methods=['POST'])
@login_required
def update_feedback():
    args = {
        'user_id': current_user.id,
        'article_id': int(request.form['article_id']),
        'opinion': request.form['opinion']
    }
    feedback = Feedback.query.filter_by(**args)
    if feedback.scalar() is not None:
        feedback.delete()
    else:
        new_feedback = Feedback(**args)
        db.session.add(new_feedback)
    db.session.commit()
    return jsonify(result='success')


if __name__ == '__main__':
    app.run()
