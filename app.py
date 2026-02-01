from data import studentLst
from studentUtils import *

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by property\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than\n8️⃣ -Add the grade\n9️⃣ -Close the app\n'

while True:
    action = input(functions)
    if action == "1":
        addStudent(studentLst)
    elif action == "2":
        formattedStudent = formattingStudent(studentLst)
        if(formattedStudent == ""):
            print("-No Students-")
        else:
            print(formattedStudent)