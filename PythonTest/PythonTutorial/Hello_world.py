#used for testing imports
#other imports

def hello_world():
    print("hello world")

class Student:
    def __init__(self, name, major, gpa, is_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_probation = is_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#inheritance
class Chef:
    def make_chicken(self):
        print("chef, make chicken!")
    def make_salad(self):
        print("chef, make salad!")

