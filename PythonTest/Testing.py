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
