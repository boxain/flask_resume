from app import create_app
from os import getenv
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.database import db,create_table,reset_table,add_new_user
from app.database.helper import forgot_password

load_dotenv()
app = create_app(getenv("FLASK_ENV"))
Migrate(app,db,render_as_batch=True) # 用sqlite最後一個參數必須設定

@app.shell_context_processor
def make_shell_context():
    return globals()
    

@app.cli.command(name="init_db")
def init_db():
    create_table()


@app.cli.command(name="reset_db")
def reset_db():
    reset_table()


@app.cli.command(name="add_new_user")
def add_user():
    name = input("Name: ")
    password = input("Password: ")
    email = input("Email: ")
    if add_new_user(name=name,password=password,email=email):
        print("OK !")
    else:
        print("Failed !")


@app.cli.command(name="modify_user")
def modify_user():
    name = input("Name: ")
    new_password = input("New Password: ")
    if forgot_password(name=name,password=new_password):
        print("OK !")
    else:
        print("Failed !")



#pbkdf2:sha256:260000$t5VGGPsbrXGCWL9E$2e1b945c5ba40b901d27b19a907a49eeb04b033ea90e6be60d39a990ab5b33b4
#pbkdf2:sha256:260000$4nQ1HDrn003qxIxm$45f10b747f4808cb407cab48783fa154fe2a656d45d6528c62964186712390bf