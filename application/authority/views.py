from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user

from application import login_manager
from .source import FormLogin, User, LightweightDirectoryAccessProtocol
from . import authority

@login_manager.user_loader
def load_user(identifier):
    user = User()
    user.id = identifier
    return user

@authority.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template(
            'authority/login.html',
            form = FormLogin()
        )
    else:
        user = request.form.get('name')
        password = request.form['password']
        if LightweightDirectoryAccessProtocol.execute(user, password):
            user = User()
            user.id = user
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            flash('Login success.')
            return redirect(next)
        else:
            flash('Login fail.')
            return render_template(
                "authority/login.html",
                form = FormLogin()
            )

@authority.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))