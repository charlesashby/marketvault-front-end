from app import app, models, db
from app.forms import user as user_forms

from sqlalchemy.exc import InvalidRequestError
from itsdangerous import URLSafeTimedSerializer

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user


ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

userbp = Blueprint('userbp', __name__, url_prefix='/user')


@userbp.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        form = user_forms.Login()
        if form.validate_on_submit():
            user = models.User.query.filter_by(email=form.email.data).first()
            if user is not None:
                if user.check_password(form.password.data):
                    login_user(user)
                    flash("Succesfully signed in", "positive")

                    return redirect(url_for('main.index'))
                else:
                    flash("The password and the email address you have entered don't match", "negative")
                    return redirect(url_for('userbp.signin'))
            else:
                flash('Unknown email address.', 'negative')
                return redirect(url_for('userbp.signin'))
        return render_template('user/signin.html', form=form, title='Sign in')
    except InvalidRequestError as e:
        print(e)
        db.session.rollback()
        return redirect(url_for('userbp.signin'))


@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    print('sign up page opened')
    form = user_forms.SignUp()
    return render_template('user/signup.html', form=form, title='Sign up')


@userbp.route('/signout')
def signout():
    logout_user()
    flash('Succesfully signed out.', 'positive')
    return redirect(url_for('index'))


@userbp.route('/account')
@login_required
def account():
    return render_template('user/account.html', title='Account')
