import Authenticate
import Tasks

auth = Authenticate.Authentication()
db = Authenticate.Database()
task = Tasks.Task()


class AskingUser:
    email = ""
    password = ""

    personal_details = {
        "Name": "",
        "Age": "",
        "Gender": "",
        "Date_of_birth"
        "Something_about_yourself": "",
    }

    def __init__(self):
        print("Hello user ..!")

    def user_choice(self):
        choice = input("What would you like to do ? \n 1.Login ? \n 2.Register \n")
        if int(choice) == 1:
            self.ask_user()
            self.login()
            self.add_task_details()
        elif int(choice) == 2:
            self.ask_user()
            self.check_for_password()
            self.registration_details()
            self.store_data()
            self.create()
        else:
            print("Enter valid info")

    def ask_user(self):
        self.email = input("Enter your Email Address please: ")
        self.password = input("Enter your password: ")

    def create(self):
        auth.create_user(self.email, self.password)
        print("Thankyou for creating account")

    def login(self):
        auth.login_user(self.email, self.password)
        print("You are succesfully logged in")

    def check_for_password(self):
        if len(self.password) <= 6:
            print("Password length is small, please make another password ")
            self.password = input("Enter password : ")
            print(self.password)
        else:
            print("password length is perfect")

    def registration_details(self):
        self.personal_details["Name"] = input('Enter your full name: ')
        self.personal_details["Age"] = input('Enter your age: ')
        self.personal_details["Gender"] = input('Enter your gender: ')
        self.personal_details["Date_of_birth"] = input('Enter you birth date(yy/mm/dd): ')
        self.personal_details["Something_about_yourself"] = input('Enter Something about yourself:')

    def store_data(self):
        db.storing_user_details(self.personal_details)
        print("Done")

    def add_task_details(self):
        task.ask_to_add()
        name = input("Doctor please enter your name again")
        db.storing_task_details(name, task.task_to_do)
        print("done")


ask_user = AskingUser()
ask_user.user_choice()
# ask_user.add_task_details()