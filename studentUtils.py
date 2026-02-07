def addStudent(studentLst):
    name = input("Enter the students name: ")
    age = input("Enter the students age: ")
    id = len(studentLst)+1
    student = {
        "id": id,
        "name" : name,
        "age" : age,
        "grades": [],
        "active": True,
    }
    studentLst.append(student)

def formattingStudent(studentLst):
    formateddStudents = ""
    for student in studentLst:
        if(student["active"]==False):
            formateddStudents = formateddStudents + "-Dropped out- "

        formateddStudents =  formateddStudents + f"Id: {student["id"]}, Name: {student["name"]}, Age: {student["age"]}\n\tGrades: "

        for grade in student["grades"]:
            formateddStudents = formateddStudents + f"{grade}, " 

        formateddStudents = formateddStudents+"\n"

    return formateddStudents

def find_by_property(studentLst, property, value):
    if(property not in ["id", "name", "age", "grades", "active"]):
        return "The property doesnt exist"
    if(property == "id"):
        value = int(value)
    if(property == "active"):
        value = bool(value)

    filteredStudents=[]
    for student in studentLst:

        print(student[property])
        if(student[property] == value):
            filteredStudents.append(student)

    return filteredStudents

def printStudents(studentLst):
    formattedStudent = formattingStudent(studentLst)
    if(formattedStudent == ""):
        print("-No Students-")
    else:
        print(formattedStudent)