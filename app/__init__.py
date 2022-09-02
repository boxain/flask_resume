from flask import Flask
from flask_login import LoginManager
from flask_pagedown import PageDown
from .email import mail
from .database import db
from .user_helper import login_manager
from .config import configs
from .main import main_bp
from .user import user_bp

login_manage = LoginManager()
pagedown = PageDown()


def create_app(env):
    app = Flask(__name__,template_folder="../templates",static_folder="../static")
    # 每次讀入pipenv環境時只會讀取一次.env檔案
    # 若.env檔案有更改就要退出pipenv shell並再次讀入
    app.config.from_object(configs[env])

    login_manage.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    # Blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    return app

