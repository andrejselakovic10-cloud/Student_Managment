from data import studentLst
from studentUtils import *

while True:
    action = input("What function are we going to commit? \n 1. Add a student \n 2. Show the student \n")
    if action == "1":
        addStudent(studentLst)
    elif action == "2":
        showStudent(studentLst)