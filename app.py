from data import studentLst
from studentUtils import *

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by property\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than n\n8️⃣ -Add the grade\n9️⃣ -Close the app\n'

while True:
    action = input(functions)
    if action == "1":
        #Provera unosa
        addStudent(studentLst)
    elif action == "2":
       printStudents(studentLst)
    elif action == "3":
        property = input("Which property do you want to search by: ")
        value = input("Which value do you want to get: ")
        filteredStudents = find_by_property(studentLst,property,value)
        if filteredStudents == None:
            continue
        printStudents(filteredStudents)
    elif action == "4":
        studentId = input("Whats the id of the student we want to remove: ")
        removedStudent = removeStudent(studentLst,studentId)
        if removedStudent == True:
            print("Succesfuly removed the student")
        else:
            print("Non-existant id")
    elif action == "5":
        sortedStudents = sortStudentsGrade(studentLst)
        pickedStudents = pickFirstStudents(sortedStudents, 3)
        if(pickedStudents == None):
            print("Not enough students in the system!")
        else:
            printStudents(pickedStudents)
    elif action == "6":
        sortedStudents = sortStudentsGrade(studentLst, False)
        pickedStudents = pickFirstStudents(sortedStudents, 3)
        if(pickedStudents == None):
            print("Not enough students in the system!")
        else:
            printStudents(pickedStudents)
    elif action == "7":
        #Show all student that have bigger grade than n
        minAvgGrade = input("Minimal average grade to sort by: ")

    elif action == "8":
        studentId = input("whats the id of the student u want to add a grade to: ")
        gradeToAdd = input("What grade are u going to add: ")
        if validGrade(gradeToAdd) == False:
            print("mrowwwwwwwwwwwwwwwwwwwwwwwwww")
            continue
        gradeSucess = gradeStudent(studentId,studentLst,gradeToAdd)
        if(gradeSucess == True):
            print("grade succesfully addded")
        else:
            print("There was an error in inplementing the requested grade. ")