from ..forms import *
from . import user_bp
from flask import render_template , redirect , url_for  , flash , request
from flask_login import login_required , current_user , logout_user , login_user
from ..database.helper import forgot_password, get_email, get_user , add_new_user
from ..email import mail
from flask_mail import Message
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@user_bp.route("/login" , methods = ["GET","POST"])
def login_page():
    if current_user.is_active:
        flash("You have logined !",category="info")
        return redirect(url_for("main.index_page"))
    else:
        form = LoginForm()
        if request.method == "GET":
            return render_template("login.html",form=form)
        if request.method == "POST":
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                if user := get_user(username=username,password=password): # 獲取該user
                    login_user(user)
                    flash("OK :)",category="info")
                    return redirect(url_for("main.index_page"))
                else:
                    flash("Wrong username or password",category="alert")
                    return redirect(url_for("user.login_page"))          
            else:
                for field , errors in form.errors.items():
                    for error in errors:
                        flash(error,category="wrong")
                return redirect(url_for("user.login_page"))
                            

@user_bp.route("/logout")
@login_required
def logout_page():
    logout_user()
    return render_template("index.html")



@user_bp.route("/register" , methods=["GET","POST"])
def register_page():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("register.html",form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.username.data
            password = form.password.data
            email = form.email.data
            if add_new_user(name=name,password=password,email=email): # 新增user
                flash("OK :)",category="info")
                return redirect(url_for("user.login_page"))
            else:
                flash("The username or email has been used",category="alert")
                return redirect(url_for("user.register_page"))

        else:
            for field , errors in form.errors.items():
                for error in errors:
                    flash(error,category="alert")
            return redirect(url_for("user.register_page"))



@user_bp.route("/forgot_password" , methods=["GET","POST"])
def forgot_password_page():
    form = ForgotForm()
    if request.method == "GET":
        return render_template("forgot_password.html",form=form)        
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.username.data
            password = form.new_password.data
            if forgot_password(name=name,password=password):
                flash("Ok :)",category="info")
                msg = Message("更改密碼",sender=getenv("MAIL_USERNAME"),recipients=[get_email(name=name)],body="成功:)")
                mail.send(message=msg)
                return redirect(url_for("user.login_page"))
            else:
                flash("Failed....",category="alert")
                return redirect(url_for("user.forgot_password_page"))
        else:
            for field , errors in form.errors.items():
                for error in errors:
                    flash(error,category="alert")
            return redirect(url_for("user.forgot_password_page"))    
        






