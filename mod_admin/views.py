from . import admin

@admin.route('/')
def admin_index():
    return 'welcome to admin index'