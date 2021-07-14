#Personally built "program" to test different features of Python
#code based on examples provided by freeCodeCamp.org: https://www.youtube.com/watch?v=rfscVS0vtbw&t=6866s

#imports
from math import *

#hello world
print("Hello World")

#print triangle
print("   /|")
print("  / |")
print(" /__|")

#variables
#string
character_name = "johno rando"
#int
this_number = 30
#float
this_float = 30.5
print ("My name is " + character_name + " and this is my story")

#string functions
print(character_name.upper())
print(character_name.lower())
print(character_name[0])
print(character_name.index("o"))
print(character_name.replace("john", "myMan"))

#prompting user
#character_name = input("Enter your name: ")

#lists/arrays
myList = ["this", "is", "my", "list"]
print("LISTS/ARRAY")
print(myList[0])
#grab all elements after array element i
print(myList[2:])
myList.remove(("is"))
print(myList)
print("number of times 'my' shows up in list: " + str(myList.count("my")))

#tuples
#tuples cannot be changed/modified
coordinates = (4, 5)
tuplist = [(1, 2), (3, 4), (5, 6)]
print(coordinates)
print("tuple: " + str(coordinates))
print(tuplist)

#functions
def sayHi(name):
    print("my function sayHi")
    print("hello " + name)
    def nested():
        print("this is my nested function")
    nested()

sayHi(character_name)

#if statements
is_cool = False
is_nice = False

if is_cool and is_nice:
    print("good job")
elif is_cool and not is_nice:
    print("bad job")
else:
    print("YOU FAIL")

#dictionary/switches, while loop
monthConvert = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConvert["Jan"])
print(monthConvert.get("not me", "INVALID"))

def number_switch(mynum):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }
    return switcher.get(mynum, "out of bounds")
i = 1
while i < 6:
    print(number_switch(i))
    print(i)
    i += 1

#for loops
for letter in "my sentence":
    print(letter)

food = ["rice", "beans", "salad"]
for each in food:
    print(each)

for index in range(len(food)):
    print(food[index])

#2-d lists and nested for loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print row 0, column 2
print(number_grid[0][2])

for row in number_grid:
    print(row)
for row in number_grid:
    for column in row:
        print(column)

#try/except
try:
    #mynum = int(input("Enter a number: "))
    mynum = 20
    print(mynum)
#zerodivision error with specific error thrown
except ZeroDivisionError as err:
    print(err)
#ValueError with specific error thrown
except ValueError as err:
    print(err)
#general catch block that is too broad - not typically used
except:
    print("general catch")

#reading from a file
# open("readfrom.txt", "r") #read only
# open("readfrom.txt", "w") #write only
# open("readfrom.txt", "a") #append
# open("readfrom.txt"), "r+") #read and write
#
# office_file = open("readfrom1.txt", "a") #opening a non-existent file creates it
# office_file.write("\nKelly:customer service")
# office_file.close()
# office_file = open("readfrom1.txt", "r")
#
# if(office_file.readable()):
#     print(office_file.read()) #read whole file

#  print(office_file.readlines()[1]) #readlines, array index 1
#  print(office_file.readline()) #read a single line

# office_file.close()

#modules fun
from Hello_world import hello_world
hello_world()

#import Student only from Hello_world
from Hello_world import Student

student1 = Student("jim", "business", 3.1, True)

print(student1.gpa)
print(student1.on_honor_roll())

from Hello_world import Chef
from specialChef import specialChef
mychef = Chef()
mychef.make_salad()

#inherited special chef class extended from chef
myspecialchef = specialChef()
myspecialchef.make_salad()
myspecialchef.make_special()