from . import main_bp
from flask import render_template , redirect , url_for , flash , request
from flask_login import login_required , current_user
from ..database.helper import get_all_comment , add_comment
from ..forms import CommentForm
from werkzeug.exceptions import HTTPException


posts = {"flask":0,
         "climb":1,
         "python":2,
         "data_analysis":3
        }

@main_bp.route('/', methods = ["GET"])
def index_page():
    '''
        首頁
    '''
    return render_template("index.html")



@main_bp.route("/resume" , methods = ["GET"])
def resume_page():
    '''
        個人履歷
    '''
    return render_template("resume.html")



@main_bp.route("/flask" , methods = ["GET","POST"])
@login_required
def flask_page():
    '''
        Flask 教學頁面
    '''
    form = CommentForm()
    comments = get_all_comment(posts["flask"]) # 讀取該貼文的所有留言
    if request.method == "GET":
        return render_template("flask.html",form=form,comments=comments)
    if request.method == "POST":
        if form.validate_on_submit:
            content = form.add_comment.data
            if add_comment(author_id=current_user.id,post_id=posts["flask"],content=content):
                flash("OK !",category="info")
            else:
                flash("Failed !",category="wrong")
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(error,category="wrong")

        return redirect(url_for("main.flask_page"))
        


@main_bp.route("/climb" , methods = ["GET"])
@login_required
def climb_page():
    '''
        爬蟲教學頁面
    '''  
    form = CommentForm()
    comments = get_all_comment(posts["climb"]) # 讀取該貼文的所有留言
    if request.method == "GET":
        return render_template("climb.html",form=form,comments=comments)
    if request.method == "POST":
        if form.validate_on_submit():
            content = form.content.data
            if add_comment(author_id=current_user.id,post_id=posts["climb"],content=content):
                flash("OK !",category="info")
            else:
                flash("Failed !",category="wrong")
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(error,category="wrong")

        return render_template("climb.html")



@main_bp.route("/python" , methods = ["GET"])
@login_required
def python_page():
    '''
        Python 教學頁面
    '''
    form = CommentForm()
    comments = get_all_comment(posts["python"]) # 讀取該貼文的所有留言
    if request.method == "GET":
        return render_template("python.html",form=form,comments=comments)
    if request.method == "POST":
        if form.validate_on_submit():
            content = form.content.data
            if add_comment(author_id=current_user.id,post_id=posts["python"],content=content):
                flash("OK !",category="info")
            else:
                flash("Failed !",category="wrong")
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(error,category="wrong")

        return render_template("python.html")



@main_bp.route("/data_analysis" , methods = ["GET","POST"])
@login_required
def data_analysis_page():
    '''
        資料分析 教學頁面
    '''
    form = CommentForm()
    comments = get_all_comment(posts["data_analysis"]) # 讀取該貼文的所有留言
    if request.method == "GET":
        return render_template("data_analysis.html",form=form,comments=comments)
    if request.method == "POST":
        if form.validate_on_submit():
            content = form.content.data
            if add_comment(author_id=current_user.id,post_id=posts["data_analysis"],content=content):
                flash("OK !",category="info")
            else:
                flash("Failed !",category="wrong")
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    flash(error,category="wrong")

        return render_template("data_analysis.html")



@main_bp.app_errorhandler(401)
def error_401(e):
    '''
        401報錯處理
    '''
    return redirect(url_for("user.login_page"))


@main_bp.app_errorhandler(HTTPException)
def error(e):
    '''
        報錯處理
    '''
    return render_template("error.html",code=e.code,name=e.name,error=e),e