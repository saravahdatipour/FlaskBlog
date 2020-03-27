from flask import request, render_template, flash

from app import db

from . import users
from .forms import RegisterForm
from .models import User


@users.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print(form.conpass)
        print(form.validate_on_submit())
        if not form.validate_on_submit():
            return render_template('user/register.html', form=form)
        print(form.password.data == form.conpass.data)
        if not form.password.data == form.conpass.data:

            error_msg="Password And Confirm Password Do not Match"
            form.password.errors.append(error_msg)
            form.conpass.errors.append(error_msg)
            return render_template('user/register.html', form=form)
        new_user = User()
        new_user.full_name = form.full_name.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("you created your account succesfully")


    return render_template('user/register.html', form=form)
