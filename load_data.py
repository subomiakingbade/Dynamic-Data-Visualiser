# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Subomi Akingbade , George Grivas, Minjun Kim"

# Update "" with your team (e.g. T102)
__team__ = "T147"

#==========================================#
# Place your student_school_list function after this line
def student_school_list (filename : str, schoolname : str) -> dict:
    """
    Returns a list of students that attended the school given
    
    Precondition : 
    
    >>>
    student_school_list("student-mat.csv","GP")
    {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
    {another element},
    """
    read_file = open (filename, "r")
    list_students = []
    for line in read_file:
        student = line.split(",")
        student[-1] = student[-1].strip()
        if student[0] == str(schoolname):
            list_students.append({"Age":int(student[1]), "StudyTime": float(student[2]), "Failures":int(student[3]), "Health":int(student[4]), "Absences":int(student[5]), "G1":int(student[6]), "G2":int(student[7]), "G3":int(student[8]), })
    read_file.close()
    return list_students



#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename:str, healthvalue:int) -> list:
    """
    This function calls and reads the value in the file, then gather the information of student who has certain health values
    
    example:
    >>> student_health_list('student-mat.csv',2)
    [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,'G1': 9, 'G2': 11, 'G3': 7},{another element},...]
    """
    file = open(filename, 'r')
    lines = file.readlines()
    headers = lines[0].strip().split(',')
    health_index = headers.index('Health')
    students = []
    for line in lines[1:]:
        values = line.strip().split(',')
        if int(values[health_index]) == healthvalue:
            student = {}
            for i in range(len(headers)):
                if i != health_index:
                    student[headers[i]] = values[i]
            students.append(student)
    file.close()
    return students

#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, age: int) -> dict:
    """returns a list of students with the same age as the imput paramater

    Preconditions: age > 0, file_name exists and is accesible

    >>> student_age_list('student-mat.csv', 15)
    {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 'G1': 7, 'G2': 8, 'G3': 10}, {another element},
    """
    read_file = open(file_name, "r")
    list_students = []   
    for line in read_file:     
        student = line.split(',')   
        student[-1] = student[-1].strip()
        if student[1] == str(age):       
            list_students.append({'School': student[0], 'StudyTime': float(student[2]), 'Failures': int(student[3]), 'Health': int(student[4]), 'Absences': int(student[5]), 'G1': int(student[6]), 'G2': int(student[7]), 'G3': int(student[8])})   
    read_file.close()
    return list_students



#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, failures: int) -> dict:
    """returns a list of students with the same number of failures as the imput paramater
    
    Precondtions: failures >= 0, filename exists and is accesible
    
    >>> student_failures_list('student-mat.csv', 0)
    {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {another element}, 
    """
    readfile = open(filename, "r")
    liststudents = []   
    for line in readfile:     
        student = line.split(',')   
        student[-1] = student[-1].strip()
        if student[3] == str(failures):       
            liststudents.append({'School': student[0], 'Age': int(student[1]), 'StudyTime': float(student[2]), 'Health': int(student[4]), 'Absences': int(student[5]), 'G1': int(student[6]), 'G2': int(student[7]), 'G3': int(student[8])})   
    readfile.close()
    return liststudents


#==========================================#
# Place your load_data function after this line
def load_data(filename:str, attributes:(str,int or str))-> list:
    """
    This function calls and reads the value in the file, bring the certain student information for valid attributes, or tell the user if the input wasn't valid
    
    example: 
    >>> load_data('student-mat.csv', ('School', 'GP'))
    [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'},{another element},...]
    """
    validattributes = ['School', 'Age', 'Health', 'Failures', 'All']
    if attributes[0] not in validattributes:
            print("Invalid Value")
            return []    
    
    file = open(filename, 'r')
    headers = file.readline().strip().split(',')
    index = headers.index(attributes[0]) if attributes[0] != 'All' else None
    studentlist = []

    for line in file:
        values = line.strip().split(',')
        if attributes[0] == 'All' or values[index] == str(attributes[1]):
            studentdict = {}
            for i in range(len(headers)):
                if i != index:
                    studentdict[headers[i]] = values[i]
            studentlist.append(studentdict)        
    file.close()
    return studentlist

#==========================================#
# Place your add_average function after this line
def add_average (students:list) -> list:
    """
    Returns the average of the students' grades G1 G2 and G3
    >>>
    add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'G1': 5, 'G2': 6, 'G3': 6}] )
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
    'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6,
    'G_Avg': 5.67 },
    """

    newaverage = 0
    if len(students) == 0:
        return students
    else:   
        for student in students: 
            gs = (student["G1"],student["G2"],student["G3"])
            newaverage = sum(gs) / 3
            student["Average"] = round(newaverage,2)
        return students




# Do NOT include a main script in your submission
