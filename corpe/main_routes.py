from flask import (render_template, url_for, flash, redirect,
                    request, Blueprint, current_app, make_response)
from corpe import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from corpe.models import Admin, Dataset

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('main/index.html')