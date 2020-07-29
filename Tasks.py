class Task:
    task_to_do = {"Monday": [""], "Tuesday": [""], "Wednesday": [""]}

    def __init__(self):
        print("Thankyou for trusting us ..!")

    def ask_to_add(self):
        print("Would you like to add some task ? ")
        choice = input("1.Yes \n2.No \n ")
        if int(choice) == 1:
            print("Which week day you want to ?")
            week_day = input("1.Monday \n 2.Tuesday \n 3.Wednesday \n")
            if int(week_day) == 1:
                self.task_to_do["Monday"] = input("Enter task to perform")
            elif int(week_day) == 2:
                self.task_to_do["Tuesday"] = input("Enter task to perform")
            elif int(week_day) == 3:
                self.task_to_do["Wednesday"] = input("Enter task to perform")
            else:
                print("Enter Valid input")
        else:
            print("Please choose a week day ")


task = Task()
task.ask_to_add()
