from flask_login import LoginManager , UserMixin
from .database.models import Users


class User(UserMixin):
    pass

login_manager = LoginManager()


@login_manager.user_loader
def load(user_id):
    user_id = int(user_id)
    user = Users.query.filter_by(id=user_id).first()
    if user:
        sessionUser = User()
        sessionUser.id = user.id
        return sessionUser
    else:
        return None

'''
上面的 load，他加上了一個 login_manager.user_loader 的裝飾器。
在這個函式裡面，我們去資料庫找到這個使用者，然後把它包裝一下變成剛剛定義的 User 的形式，
這樣 Flask-Login 才看得懂，而如果這個使用者不存在的話，那就回傳 None，這是官方文件指示的。
'''