from flask import Blueprint

facebook_login_bp = Blueprint('facebook_login', __name__)

from backend.facebook_login import routes
