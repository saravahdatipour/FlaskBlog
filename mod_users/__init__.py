from flask import Blueprint
from .models import User
users = Blueprint('users',__name__,url_prefix='/users/')

