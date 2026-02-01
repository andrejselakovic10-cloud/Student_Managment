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