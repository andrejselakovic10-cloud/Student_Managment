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
# studentlst = array
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
# stidentlst - arary
def find_by_property(studentLst, property, value):  # studentlst - array, property - string, value = str
    if(property not in ["id", "name", "age", "grades", "active"]):
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
#studentLst = array, id = str
def averageGrade(student):
    #student = find_by_property(studentLst, "id", id)
    #if student == None:
    #    return False
    #Mi znamo da student nije NONE
    #student = [{...}]
    #student = student[0]
    #student = {..., "grades": []}
    sum = 0
    noGrades = len(student["grades"])
    for grade in student["grades"]:
        sum = sum+grade

    return sum / noGrades

def bestGradesOfAll(studentLst):
    averageGrades = []
    for student in studentLst:
        averageGrades.append({
            "id":student["id"],
            "avgGrade":averageGrade(student)
        })

    sortedStudents = sorted(averageGrades, key=lambda x: x["avgGrade"],reverse=True)
    bestStudents = [
        find_by_property(studentLst,"id", sortedStudents[0]["id"])[0],
        find_by_property(studentLst,"id", sortedStudents[1]["id"])[0],
        find_by_property(studentLst,"id", sortedStudents[2]["id"])[0]
    ]
    
    return formattingStudent(bestStudents)