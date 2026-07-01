from flask import render_template, redirect, url_for, flash, request
from urllib.parse import urlsplit
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
                           SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
                            URL

from ..models.user import User
from ..models.profile import Profile


from flask import Blueprint
bp = Blueprint('main_form', __name__)

"""
Forms for user information, i.e. login, registration, etc.
"""


class Status(FlaskForm):
    """
    Status Form
    """
    submit = SubmitField('Submit')


@bp.route('/Status', methods=['GET', 'POST'])
def StatusForm():
    """
    Login page. Reached from login link on home page (index).

    Uses GET to allow form to be filled in. Uses POST to attempt login.
    Valid form credentials check for user in database. If user not found
    or a database error occurs, flash an error and return (redirect) to
    this page. If the user is found then login user (via flask_login) and
    reload home page. Invalid form credentials force the form to be reloaded.
    """

    status_form = Status()
    
    if request.method == 'POST':
        name = request.form.get('q1_name')
        ok = request.form.get('q2_ok')
        safety = request.form.get('q3_safety')
        need_help = request.form.get('q4_need_help')
        optional_surroundings = request.form.get('q5_optional_surroundings')
        final_notes = request.form.get('q6_final_notes')

        # do something with the data — e.g. save to a database
       # print(pain, eaten, medication)

        return redirect(url_for('main_form.thank_you'))

    return render_template('StatusForm.html', form=status_form)

@bp.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')
    
    
    
    
    
    
    
    
    
    
    """
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    status_form = StatusForm()
    if status_form.validate_on_submit():
        try:
            user = User.get_from_status(login_form.email.data,
                                       login_form.password.data)
        except Exception as e:
            flash(str(e))
            return redirect(url_for("users.login"))

        if user is None:
            flash('Invalid email or password')
            return redirect(url_for('users.login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index.index')

        return redirect(next_page)

    return render_template('login.html', title='Log In', form=login_form)

"""



@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Allow user to register themselvew. Reached from registration link on home
    page (index) or from login page. Users cannot register as administrators

    Uses GET to allow form to be filled in. Uses POST to attempt registration.
    Valid form credentials attempt to add user to database. Successful
    registration redirects to the login page. Unsucessful registration reloads
    the registration page.
    """

    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        if User.register(reg_form.email.data,
                         reg_form.password.data,
                         reg_form.first_name.data,
                         reg_form.last_name.data, False):
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=reg_form)


""" Profile forms """


