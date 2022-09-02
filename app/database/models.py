from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash , check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    # 表名用小寫
    __tablename__ = "users"
    # 有了前面兩個型態設定，autoincreament會自動存在
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50) , nullable=False)
    password = db.Column(db.String(200) , nullable=False)
    email = db.Column(db.String(50) , nullable=False)
    register_time = db.Column(db.DateTime , default=datetime.now , nullable=False)
    comment = db.relationship("Comments")

    def __init__(self,name,password,email) -> None:
        self.name = name
        self.password = generate_password_hash(password)
        self.email = email

    def check_password(self,password):
        return check_password_hash(self.password,password)


class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer , primary_key=True)
    author_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    post_id = db.Column(db.Integer , nullable=False)
    content = db.Column(db.String(50) , nullable=False)
    time = db.Column(db.DateTime , default=datetime.now , nullable=False)

    def __init__(self,author_id,post_id,content) -> None:
        self.author_id = author_id
        self.post_id = post_id
        self.content = content
    