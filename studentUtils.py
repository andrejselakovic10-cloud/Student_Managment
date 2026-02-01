
def addStudent(studentLst):
    name = input("Enter the students name: ")
    age = input("Enter the students age: ")
    student = {
        "name" : name,
        "age" : age 
    }
    studentLst.append(student)
def showStudent(studentLst):
    for student in studentLst:
        print(f"{student["name"]}, age: {student["age"]}")