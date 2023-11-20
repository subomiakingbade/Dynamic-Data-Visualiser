# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Subomi Akingbade , George Grivas, Minjun Kim, Shayla Kellet"

# Update "" with your team (e.g. T102)
__team__ = "T147"

#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(students: list, sort: str) -> list:
    """Returns the sorted list of students in either ascending or descending order.

    Preconditions: sort == "A" or sort == "D", students contains "Age".

    Example:
sort_students_age_bubble(
        [{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")

    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")

    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]

    >>> sort_students_age_bubble(
        [{"Age":18,"School":"GP"},{"Age":14,"School":"MS"},{"Age":29,"School":"AB"}], "A")

    [{'Age': 14, 'School': 'MS'}, {'Age': 18, 'School': 'GP'}, {'Age': 29, 'School': 'AB'}]
    """ 

    length = len(students)

    if any("Age" in keys for keys in students):
        for x in range(length - 1):
            for y in range(length - x - 1):
                if(sort == "A"):
                    if(students[y]["Age"] > students[y + 1]["Age"]):
                        students[y], students[y + 1] = students[y + 1], students[y]

                elif(sort == "D"):
                    if(students[y]["Age"] < students[y + 1]["Age"]):
                        students[y], students[y + 1] = students[y + 1], students[y]

    else:
        print('"Age" key is not present')

    return students

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students: list[dict], order: str) -> list[dict]:
    """returns the ascending or descending sorted list of students based on their study time
    
    Preconditions: order == "A" or "D"
    
    
    >>> sort_students_time_selection([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]
  
    >>>sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    """

    if any("StudyTime" in keys for keys in students):
        for i in range(len(students)):
            min_idx = i
            for j in range(i + 1, len(students)):
                if students[min_idx]["StudyTime"] > students[j]["StudyTime"]:
                    min_idx = j 
            
            students[i], students[min_idx] = students[min_idx], students[i]
                    
        if order == "A":
            return students
        elif order == "D":
            return students[::-1]
                                     
    else:
        print('"StudyTime" key is not present')
    return students


#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(students: list[dict], order: str)-> list[dict]:
    """
    This function arranges a collection of student dictionaries based on their G_Avg values using the insertion sort algorithm.
    
    Example: 
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]
    """
    for i in range(1, len(students)):
        key = students[i]
        I = i - 1
        if "G_Avg" not in key:
            print ("'G_Avg' key is not present")
            return students            
        if order == "A":
            while I >= 0 and students[j]["G_Avg"] > key["G_Avg"]:
                students[j + 1] = students[j]
                I -= 1
        else:
            while I >= 0 and students[I]["G_Avg"] < key["G_Avg"]:
                students[I + 1] = students[I]
                I -= 1
        students[I + 1] = key

    return students

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(students : list, order: str) -> list:
    """
    Returns a list of student failures sorted in acsending or descending order
    depending on the input
    
    Precondition: len (list) > 0 , order must be inputted
    
    >>>sort_students_failures_bubble(
    [{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]
    
    """
    if "Failures" not in students [0]:
        print ("Failures key is not present")
        return students
    
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if order == "A":
                if students[j]["Failures"] > students[j+1]["Failures"]:
                    students[j], students[j + 1] = students[j + 1], students[j]
            elif order == "D":
                if students[j]["Failures"] < students[j+1]["Failures"]:
                    students[j], students[j + 1] = students[j + 1], students[j]
            else:
                print("Input A for ascending order and D for descending")
                return students
    return students          
        


#==========================================#
# Place your sort function after this line

def sort(students : list[dict], order : str, sorttype : str) -> list[dict]:
    """
    Returns a sorted list depending on the order given and what the list should
    be sorted by
    
    precondition order == "A" or "D"
    
    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]
    """
    
    if sorttype not in ["Age", "StudyTime", "G_Avg", "Failures"]:
        print ("Cannot be sorted by", attribute)
        return students
    
    
    elif sorttype == "Age":
        if order == "A":
            sortedlst = sort_students_age_bubble(students,"A")
        elif order == "D":
            sortedlst = sort_students_age_bubble(students,"D")
        else:
            print("Input A for ascending order and D for descending")
            return students 
        
        
    elif sorttype == "StudyTime":
        if order == "A":
            sortedlst = sort_students_time_selection(students, "A")
        elif order == "D":
            sortedlst = sort_students_time_selection(students, "D")
        else:
            print("Input A for ascending order and D for descending")
            return students         


    elif sorttype == "G_Avg":
        if order == "A":
            sortedlst = sort_students_g_avg_insertion(students, "A")
        elif order == "D":
            sortedlst = sort_students_g_avg_insertion(students, "D")
        else:
            print("Input A for ascending order and D for descending")
            return students     


    elif sorttype == "Failures":
        if order == "A":
            sortedlst = sort_students_failures_bubble(students, "A")
        elif order == "D":
            sortedlst = sort_students_failures_bubble(students, "D")
        else:
            print("Input A for ascending order and D for descending")
            return students   
    return sortedlst

# Do NOT include a main script in your submission
