from os import getenv
from os import urandom
from dotenv import load_dotenv

load_dotenv() # load enviroment_variables

class Config:
    # Flask-Mail
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD")
    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class Development(Config):
    # Flask 
    ENV = "DEVELOPMENT"
    DEBUG = True
    SECRET_KEY = "aaronsecreykey0919"
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/data.db"


class Testing(Config):
    # Flask
    ENV = "TESTING"
    TESTING = True
    SECRET_KEY = "aaronsecreykey0919"
    SERVER_NAME = "localhost"
    # Flask-SQLAlchemy
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/data.db"
    # Flask-WTF
    WTF_CSRF_ENABLED = False


class Production(Config):
    # Flask
    ENV = "PRODUCTION"
    SECRET_KEY = urandom(32)
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")
    # 不確定是否能放在別的目錄外

# 要小寫
configs = {
    "testing":Testing,
    "development":Development,
    "production":Production
}