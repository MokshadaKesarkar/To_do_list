import pyrebase


config = {
    "apiKey": "AIzaSyCMVAS1aLI4xkZz8AJ8cMiAtW0w1LtW1zc",
    "authDomain": "to-do-list-993ed.firebaseapp.com",
    "databaseURL": "https://to-do-list-993ed.firebaseio.com",
    "projectId": "to-do-list-993ed",
    "storageBucket": "to-do-list-993ed.appspot.com",
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()


class Authentication:

    @staticmethod
    def create_user(email, password):
        auth.create_user_with_email_and_password(email, password)

    @staticmethod
    def login_user(email, password):
        auth.sign_in_with_email_and_password(email, password)


class Database:

    @staticmethod
    def storing_user_details(personal_details):
        db.child("users").child(personal_details["Name"]).set(personal_details)

    # @staticmethod
    # def storing_task_details( name, task_to_do):
    #     db.child('users').child(name).child('Tasks').child(["task_to_do"]).set(task_to_do)