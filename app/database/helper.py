from .models import db , Users , Comments
from ..user_helper import User
from werkzeug.security import generate_password_hash
from app import mail

def create_table():
    db.create_all()


def reset_table():
    db.drop_all()
    db.create_all()


def add_new_user(name,password,email):
    user = Users(name=name,password=password,email=email)
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except ValueError as v:
        print("錯誤: ",v)
        return False


def get_user_name(user_id):
    return Users.query.filter_by(id=user_id).first().name


def render_comment(comment_id):
    comment = Comments.query.filter_by(id=comment_id).first()
    res = {
        "name":get_user_name(user_id=comment.author_id), 
        "time":comment.time,
        "content":comment.content
    }
    return res


def get_all_comment(post_id):
    comments = Comments.query.filter_by(post_id=post_id).all()
    comments_id = [comment.id for comment in comments]
    return list(map(render_comment,comments_id))


def add_comment(author_id,post_id,content):
    comment = Comments(author_id=author_id,post_id=post_id,content=content)
    try:
        db.session.add(comment)
        db.session.commit()
        return True
    except:
        return False


def get_user(username,password):
    if user := Users.query.filter_by(name=username).first():
        if user.check_password(password=password):
            sessionUser = User()
            sessionUser.id = user.id
            return sessionUser
    
    return False


def forgot_password(name,password):
    if user := Users.query.filter_by(name=name):
        data = {"password":generate_password_hash(password)}
        try:
            user.update(data)
            db.session.commit()
            return True
        except ValueError as e:
            print(e)
            return False
    else:
        print("找不到使用者!!")



def get_email(name):
    user = Users.query.filter_by(name=name).first()
    return user.email
    
        