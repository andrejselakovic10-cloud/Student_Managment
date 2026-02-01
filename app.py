from data import studentLst
from studentUtils import *

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by property\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than\n8️⃣ -Add the grade\n9️⃣ -Close the app\n'

while True:
    action = input(functions)
    if action == "1":
        addStudent(studentLst)
    elif action == "2":
       printStudents(studentLst)
    elif action == "3":
        property = input("Why property do you want to search by: ")
        value = input("Why value do you want to get: ")
        filteredStudents = find_by_property(studentLst,property,value)
        printStudents(filteredStudents)
        #Dva studenta kada se unesu i active testiramo onda dobijemo gresku