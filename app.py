from data import studentLst
from studentUtils import *

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by property\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than n\n8️⃣ -Add the grade\n9️⃣ -Close the app\n'

##DOMACI
#Proveri zasto u akciji broj 7, se ispisuju 2 puta studenti
#Napravi proveru za specijalne karaktere za ime. Space mora da postoji

while True:
    action = input(functions)
    if action == "1": #Add student
        if addStudent(studentLst) == False:
            print("Error whilst adding the student(invalid inputed data)")
        else:
            print("Successfully added the student")
    elif action == "2": # Show all students
       printStudents(studentLst)
    elif action == "3": #Find student by property
        property = input("Which property do you want to search by: ")
        value = input("Which value do you want to get: ")
        filteredStudents = find_by_property(studentLst,property,value)
        if filteredStudents == None:
            continue
        printStudents(filteredStudents)
    elif action == "4": #Delete student
        studentId = input("Whats the id of the student we want to remove: ")
        removedStudent = removeStudent(studentLst,studentId)
        if removedStudent == True:
            print("Succesfuly removed the student")
        else:
            print("Non-existant id")
    elif action == "5": #Show 3 best students by grade
        sortedStudents = sortStudentsGrade(studentLst)
        pickedStudents = pickFirstStudents(sortedStudents, 3)
        if(pickedStudents == None):
            print("Not enough students in the system!")
        else:
            printStudents(pickedStudents)
    elif action == "6": #Show 3 worst students by grade
        sortedStudents = sortStudentsGrade(studentLst, False)
        pickedStudents = pickFirstStudents(sortedStudents, 3)
        if(pickedStudents == None):
            print("Not enough students in the system!")
        else:
            printStudents(pickedStudents)
    elif action == "7": #Show all student that have bigger average grade than n
        averageGrades = getStudentAvrageGrade(studentLst)
        
        minAvgGrade = input("Minimal average grade to sort by: ")
        if validGrade(minAvgGrade) == False:
            print("The grade you entered is not valid!")
            continue

        biggerGradeThan = []
        for student in averageGrades:
            if student["avgGrade"] >= int(minAvgGrade):
                biggerGradeThan.append(student)
        
        pickedStudents = []
        for student in biggerGradeThan:
            pickedStudents.append(student["student"])
                
        print(f"student with a grade higher than that:\n{printStudents(pickedStudents)}")
        
    elif action == "8": #Add the grade
        studentId = input("whats the id of the student u want to add a grade to: ")
        gradeToAdd = input("What grade are u going to add: ")
        if validGrade(gradeToAdd) == False:
            print("the number you inputted is invalid")
            continue
        gradeSucess = gradeStudent(studentId,studentLst,gradeToAdd)
        if(gradeSucess == True):
            print("Grade successfully added")
        else:
            print("There was an error in inplementing the requested grade. ")