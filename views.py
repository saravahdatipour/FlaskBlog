from flask import session
from app import app

@app.route('/')
def index():
    return "hello world"

