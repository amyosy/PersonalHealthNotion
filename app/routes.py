from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from .models import User, HealthData
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')


@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Registrierung implementieren
        flash('Account created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        # Login implementieren
        flash('Login successful!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', title='Login', form=form)


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@main.route("/goals")
@login_required
def goals():
    return render_template('goals.html', title='Goals')


@main.route("/reminders")
@login_required
def reminders():
    return render_template('reminders.html', title='Reminders')
