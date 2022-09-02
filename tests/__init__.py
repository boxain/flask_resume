import os,sys
import unittest
sys.path.append(os.getcwd())
from app import create_app
from app.database import db
from flask import url_for
import json

class ConfigTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()        
        self.user_register_data = {
            "username":"test_user",
            "password":"test123",
            "repeat_password":"test123",
            "email":"test123@gmail.com"    
        }
        self.user_login_data = {
            "username":"test_user",
            "password":"test123"
        }
        db.create_all()


    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        if self.app_context is not None:
            self.app_context.pop()


    def test_user_register(self): # 註冊是否成功
        return self.client.post(url_for("user.register_page"),data=self.user_register_data)



    def test_user_login(self): # 登入是否成功
        return self.client.post(url_for("user.login_page"),data=self.user_login_data)
    

    def test_resume(self): # 是否能進resume
        response = self.client.get(url_for("main.resume_page"),follow_redirects=True)
        return self.assertEqual(response.status_code,200)
        


    def test_flask(self): # 是否能進flask
        response = self.client.get(url_for("main.flask_page"),follow_redirects=True)
        return self.assertEqual(response.status_code,200)


    def test_climb(self): # 是否能進climb
        response = self.client.get(url_for("main.climb_page"),follow_redirects=True)
        return self.assertEqual(response.status_code,200)


    def test_python(self): # 是否能進python
        response = self.client.get(url_for("main.python_page"),follow_redirects=True)
        return self.assertEqual(response.status_code,200)


    def test_data_analysis(self): # 是否能進資料分析
        response = self.client.get(url_for("main.data_analysis_page"),follow_redirects=True)
        return self.assertEqual(response.status_code,200)
 

if __name__ == '__main__':
    unittest.main()