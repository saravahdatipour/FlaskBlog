from flask import session
from app import app

@app.route('/')
def index():
    return "hello world"

@app.route('/login/')
def login():
    session['name']='sara'
    print(session)
    return '1'