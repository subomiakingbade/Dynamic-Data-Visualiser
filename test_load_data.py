# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Subomi Akingbade , George Grivas, Minjun Kim"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T147"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    # Test student_school_list() function
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'GP'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'MB'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'CF'), list), True)
    
    # Test student_age_list() function
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 15), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 16), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 17), list), True)
    
    # Test student_health_list() function
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 1), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 5), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 4), list), True)
    
    # Test student_failures_list() function
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 0), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 1), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 2), list), True)
    
    # Test load_data() function
    check.equal(isinstance(load_data.load_data('student-test.csv', ('School', 'GP')), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Age', 18)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Health', 3)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Study time', 2.0)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Failures', 0)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Abesence', 6)), list), True)  
    
    # Test add_average() function
    check.equal(isinstance(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6,'G1': 5,'G2': 6,'G3': 6}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5,'G2': 5,'G3': 5}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6,'G1': 5,'G2': 9,'G3': 7}]), list), True)


# Place test_return_list_correct_lenght function here
def test_return_list_correct_length():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    assert len(load_data.student_school_list("student-test.csv","GP")) == 3 
    assert len(load_data.student_school_list("student-test.csv","MB")) == 2
    assert len(load_data.student_school_list("student-test.csv","CF")) == 3
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    assert len(load_data.student_age_list("student-test.csv","16")) == 2
    assert len(load_data.student_age_list("student-test.csv","17")) == 6
    assert len(load_data.student_age_list("student-test.csv","18")) == 4
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    assert len(load_data.student_health_list("student-test.csv","1")) == 1
    assert len(load_data.student_health_list("student-test.csv","2")) == 0
    assert len(load_data.student_health_list("student-test.csv","3")) == 8    
    
    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    assert len(load_data.student_failures_list("student-test.csv","0")) == 11
    assert len(load_data.student_failures_list("student-test.csv","1")) == 1
    assert len(load_data.student_failures_list("student-test.csv","2")) == 2
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    assert len(load_data.load_data("student-test.csv",("School","GP"))) == 3
    assert len(load_data.load_data("student-test.csv",("Age","16"))) == 2        
    assert len(load_data.load_data("student-test.csv",("Failures","0"))) == 11
        
    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    assert len(load_data.add_average([ {"School": 'GP','Age': 18,'StudyTime': 2,'Failures': 0,'Health': 3,'Absences': 6,'G1':5,'G2':6,'G3':6}])) == 5.67
    assert len(load_data.add_average([ {"School": 'GP','Age': 17,'StudyTime': 2,'Failures': 0,'Health': 3,'Absences': 4,'G1':5,'G2':5,'G3':6}])) == 5
    assert len(load_data.add_average([ {"School": 'GP','Age': 15,'StudyTime': 2,'Failures': 3,'Health': 3,'Absences': 10,'G1':7,'G2':8,'G3':10}])) == 7.67
    check.summary()


#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    #Complete the function with your test cases
   
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    schoolTestOne = student_school_list("student-test.csv", "GP")
    check.equal(schoolCheckOne[0], "{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}")
 
    schoolTestTwo = student_school_list("student-test.csv", "CF")
    check.equal(schoolCheckOne[1], "{'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}")
 
    schoolTestThree = student_school_list("student-test.csv", "MS")
    check.equal(schoolCheckOne[3], "{'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}")       
    
    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    ageTestOne = student_age_list("student-test.csv", 18)
    check.equal(schoolCheckOne[0], "{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}")
 
    ageTestTwo = student_age_list("student-test.csv", 15)
    check.equal(schoolCheckOne[1], "{'School': 'MB', 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}")
 
    ageTestThree = student_age_list("student-test.csv", 16)
    check.equal(schoolCheckOne[0], "{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}")    
    
    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    healthTestOne = student_health_list("student-test.csv", 1)
    check.equal(schoolCheckOne[0], "{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33}")
   
    healthTestTwo = student_health_list("student-test.csv", 5)
    check.equal(schoolCheckOne[2], "{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.67}")
   
    healthTestThree = student_health_list("student-test.csv", 3)
    check.equal(schoolCheckOne[3], "{'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}")   
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    failureTestOne = student_failures_list("student-test.csv", 0)
    check.equal(schoolCheckOne[0], "{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}")
   
    failureTestTwo = student_failures_list("student-test.csv", 1)
    check.equal(schoolCheckOne[0], "{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}")
   
    failureTestThree = student_failures_list("student-test.csv", 2)
    check.equal(schoolCheckOne[1], "{'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 6, 'G_Avg': 6.67}")      
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    loadTestOne = load_data("student-test.csv", ("School", "GP"))
    check.equal(schoolCheckOne[0], "{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}")
   
    loadTestTwo = load_data("student-test.csv", ("All", -1))
    check.equal(schoolCheckOne[3], "{'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}")
   
    loadTestThree = load_data("student-test.csv", ("Failures", 3))
    check.equal(schoolCheckOne[0], "{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}")
   
    loadTestFour = load_data("student-test.csv", ("Health", 5))
    check.equal(schoolCheckOne[2], "{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}")
   
    loadTestFive = load_data("student-test.csv", ("Age", 16))
    check.equal(schoolCheckOne[1], "{'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}")
   
    loadTestSix = load_data("student-test.csv", ("Age", 18))
    check.equal(schoolCheckOne[3], "{'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}")   
    
    #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
    averageTestOne = add_average(schoolTestOne)
    check.equal(schoolCheckOne[0], "{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}")
    
    averageTestTwo = add_average(loadTestSix)
    check.equal(schoolCheckOne[3], "{'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}")
    
    averageTestThree = add_average(healthTestThree)
    check.equal(schoolCheckOne[3], "{'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}")   
    check.summary()



#Place test_add_average function here
def test_add_average():
    #Complete the function with your test cases
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    lst = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'G1': 5, 'G2': 6, 'G3': 6},{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length = len(lst)
    lst2 = load_data.add_average(lst)
    check.equal(len(lst2), (old_length))
    
    lst3 = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length2 = len(lst3)
    lst4 = load_data.add_average(lst3)
    check.equal(len(lst4), (old_length2))
    
    lst5 = [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length3 = len(lst5)
    lst6 = load_data.add_average(lst5)
    check.equal(len(lst6), (old_length3))
    
    lst7 = [{'School': 'GP', 'Age': 19, 'StudyTime': 6.8, 'Health': 2, 'Absences': 8, 'G1': 13, 'G2': 14, 'G3': 15}, {'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length4 = len(lst7)
    lst8 = load_data.add_average(lst7)
    check.equal(len(lst8), (old_length4))
    
    lst9 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    old_length5 = len(lst9)
    lst10 = load_data.add_average(lst9)
    check.equal(len(lst10), (old_length5))    
    #test that the function returns an empty list when it is called whith an empty list
    
    lst11 = []    
    old_length6 = len(lst11)
    lst12 = load_data.add_average(lst11)
    check.equal(len(lst12), (old_length6))    
    
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    lst14 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst14:
        nokeys1 = len(student)
    
    lst15 = load_data.add_average(lst14)
    for student in lst15:
        nokeys2 = len(student)    
    check.equal(nokeys1, (nokeys2-1))     
    
    
    
    lst18 = [{'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst18:
        nokeys3 = len(student)
    
    lst19 = load_data.add_average(lst18)
    for student in lst19:
        nokeys4 = len(student)    
    check.equal(nokeys3, (nokeys4-1))     
    
    
    
    lst20 = [{'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst20:
        nokeys5 = len(student)
    
    lst21 = load_data.add_average(lst20)
    for student in lst21:
        nokeys6 = len(student)    
    check.equal(nokeys5, (nokeys6-1))     
    
    
    
    lst22 = [{'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst22:
        nokeys7 = len(student)
    
    lst23 = load_data.add_average(lst22)
    for student in lst23:
        nokeys8 = len(student)    
    check.equal(nokeys7, (nokeys8-1))     
    
    
    
    lst24 = [{'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst24:
        nokeys9 = len(student)
    
    lst25 = load_data.add_average(lst24)
    for student in lst25:
        nokeys10 = len(student)    
    check.equal(nokeys9, (nokeys10-1))         
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    lst16 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}]
    for student in lst16:
        gs = (student["G1"],student["G2"],student["G3"])
        newaverage = sum(gs) / 3
    lst17 = load_data.add_average(lst16)
    for student in lst17:
        gs2 = (student["G1"],student["G2"], student["G3"])
        newaverage2 = sum(gs2) / 3  
    check.equal(newaverage, newaverage2)
    
    

    lst26 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 13, 'G2': 14, 'G3': 15}]
    for student in lst26:
        gs3 = (student["G1"],student["G2"],student["G3"])
        newaverage3 = sum(gs3) / 3
    lst27 = load_data.add_average(lst26)
    for student in lst27:
        gs4 = (student["G1"],student["G2"], student["G3"])
        newaverage4 = sum(gs4) / 3  
    check.equal(newaverage3, newaverage4)
    
    
    
    lst28 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 14, 'G2': 15, 'G3': 16}]
    for student in lst28:
        gs5 = (student["G1"],student["G2"],student["G3"])
        newaverage5 = sum(gs5) / 3
    lst29 = load_data.add_average(lst28)
    for student in lst29:
        gs6 = (student["G1"],student["G2"], student["G3"])
        newaverage6 = sum(gs6) / 3  
    check.equal(newaverage5, newaverage6)
    
    
    
    lst30 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 15, 'G2': 16, 'G3': 17}]
    for student in lst30:
        gs7 = (student["G1"],student["G2"],student["G3"])
        newaverage7 = sum(gs7) / 3
    lst31 = load_data.add_average(lst30)
    for student in lst31:
        gs8 = (student["G1"],student["G2"], student["G3"])
        newaverage8 = sum(gs8) / 3  
    check.equal(newaverage7, newaverage8)
    
    
    
    lst32 = [{'school': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 16, 'G2': 17, 'G3': 18}]
    for student in lst32:
        gs9 = (student["G1"],student["G2"],student["G3"])
        newaverage9 = sum(gs9) / 3
    lst33 = load_data.add_average(lst32)
    for student in lst33:
        gs10 = (student["G1"],student["G2"], student["G3"])
        newaverage10 = sum(gs10) / 3  
    check.equal(newaverage9, newaverage10)    
    check.summary()


# Do NOT include a main script in your submission
