#user_routes.py

from flask import Blueprint, render_template

user_bp = blueprint('user', _name_ url_profix = '/users')
create_user_bp = Blueprint('create_usuarios,' _name_)

@user_bp.route('/')
def users():
    return render_template('usuarios.html')

@create_user_bp.route('users/create_usuarios')
def create_users():
    return render_template("create_users.html")