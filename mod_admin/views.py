from . import admin

@admin.route('/')
def admin_index():
    return 'welcome to admin index'

@admin.route('/login/')
def login():
    session['name']='sara'
    print(session)
    return '1'