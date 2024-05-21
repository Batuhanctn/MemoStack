import firebase_admin  # pip install firebase-admin
from firebase_admin import credentials, db
import pyrebase  # pip install pyrebase4
from flask import Flask,render_template,request

class Firebase:
    def __init__(self):
        CREDENTIALS_FILE = "C:\\Users\Win10\\Desktop\\fırebase\\firebase\\credentials.json"
        DATABASE_URL = "https://fir-dc6c9-default-rtdb.europe-west1.firebasedatabase.app"
        API_KEY = "AIzaSyCKkKUNn5cVNLGax8Zs7pUlreZ29tRgAJk"
        PROJECT_ID = "fir-dc6c9"
        self.cred = credentials.Certificate(CREDENTIALS_FILE)
        firebase_admin.initialize_app(
            self.cred,
            {
                "databaseURL": DATABASE_URL,
            },
        )
        self.ref = db.reference("/")
        self.config = {
            "apiKey": API_KEY,
            "authDomain": f"{PROJECT_ID}.firebaseapp.com",
            "databaseURL": DATABASE_URL,
            "storageBucket": f"{PROJECT_ID}.appspot.com",
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        
    def login(self, email, password):
        self.auth.sign_in_with_email_and_password(email, password)

    def register(self, email, password):
        self.auth.create_user_with_email_and_password(email, password)
            
    def get_current_user(self):
            return self.auth.current_user

    def get_user_id(self):
        return self.auth.current_user["localId"]

    def get_user_email(self):
        return self.auth.current_user["email"]

    def logout(self):
        self.auth.current_user = None
       