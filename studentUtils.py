def addStudent(studentLst):
    name = input("Enter the students name: ")
    if validName(name) == False:
        return False
    birthYear = input("Enter the students birth year: ")
    if validBirthYear(birthYear) == False:
        return False
    id = len(studentLst)+1
    student = {
        "id": id,
        "name" : name,
        "birthYear" : birthYear,
        "grades": [],
        "active": True,
    }
    studentLst.append(student)
    return True
# studentlst = array
def formattingStudent(studentLst):
    formateddStudents = ""
    for student in studentLst:
        if(student["active"]==False):
            formateddStudents = formateddStudents + "-Dropped out- "

        formateddStudents =  formateddStudents + f"Id: {student["id"]}, Name: {student["name"]}, birth Year: {student["birthYear"]}\n\tGrades: "

        for grade in student["grades"]:
            formateddStudents = formateddStudents + f"{grade}, " 

        formateddStudents = formateddStudents+"\n"

    return formateddStudents
# stidentlst - arary
def find_by_property(studentLst, property, value):  # studentlst - array, property - string, value = str
    if(property not in ["id", "name", "birthYear", "grades", "active"]):
        print("The property doesnt exist")
        return None
    
    if(property == "id"):
        value = int(value)
    if(property == "active"):
        if value == "false":
            value = False
        elif value == "true":
            value = True
        else:
            print("error")
            return None
        
    filteredStudents=[]
    for student in studentLst:
        print(student[property])
        if(student[property] == value):
            filteredStudents.append(student)

    return filteredStudents
# studentlst = array
def printStudents(studentLst):
    formattedStudent = formattingStudent(studentLst)
    if(formattedStudent == ""):
        print("-No Students-")
    else:
        print(formattedStudent)
# studentlst = array, studentid = str
def removeStudent(studentLst,studentId):
    for student in studentLst:
        if int(studentId) == student["id"]:
            student["active"] = False
            return True
        
    return False 
# studentid - str,studentlst = array, gradetoadd = str
def gradeStudent(studentId,studentLst,gradeToAdd):
    for student in studentLst:
        if(int(studentId) == student["id"]):
            student["grades"].append(int(gradeToAdd))
            return True
    return False 
#studentLst = array
def averageGrade(student):

    sum = 0
    noGrades = len(student["grades"])
    for grade in student["grades"]:
        sum = sum+grade

    return sum / noGrades

#studentLst = lsit o student, best = boolean
def sortStudentsGrade(studentLst, best = True ):
    averageGrades = []
    for student in studentLst:  #Ovde prolazimo kroz sve nase studente (1 milion studenta)( milion operacija)
        averageGrades.append({
            "student" : student,
            "avgGrade": averageGrade(student)
        })

    sortedGrades = sorted(averageGrades, key=lambda x: x["avgGrade"],reverse=best)
    sortedStudents = []
    for studentGrade in sortedGrades:
        sortedStudents.append(studentGrade["student"])

    
    return sortedStudents

#studentLst = string, n = int
def pickFirstStudents(studentLst, n):
    
    pickedStudents = []

    if n>len(studentLst) or n==0:
        return None

    for i in range(n):
        pickedStudents.append(studentLst[i])

    return pickedStudents
# grade = str
def isStrInt(str):
    str = str.strip()
    if str.isdigit() == False:
        return None
    else:
        return int(str)
def validGrade(grade):
    grade = isStrInt(grade)
    if grade == None:
        return False
    if grade != round(grade):        #decomals
        return False
    if grade > 0 and grade < 6:
        return True
    
    return False 
def validBirthYear(birthYear):
    birthYear = isStrInt(birthYear)
    if birthYear == None:
        return False
    if birthYear > 1900 and birthYear < 2026:
        return True
    return False
# name = str
def validName(name):
    name = name.strip()
    spaceCount = name.count(" ")   
    if spaceCount != 2 and spaceCount!= 1:                               # get rid of ones w special characters wihout removing space
        return False
    for character in name:
        if character.isdigit():                 # numbress
            return False
    return True