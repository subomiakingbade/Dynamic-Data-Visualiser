# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Subomi Akingbade"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261502"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-147"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt

def histogram (students : list, att: str):
    
    values = [student[att]for student in students]

        
    if type(values[0]) == int:
        bins = range(min(values), max(values)+2)
    
    elif type(values[0]) == float:
        bins = plt.hist(values, bins = "auto") [1]
        
    else:
        sortedvalues = sorted(set(values))
        bins = range(len(sortedvalues))
        plt.hist(values, bins)
        plt.xticks(range(len(sortedvalues)), sortedvalues)
        
    numbr = []
    for i in range (len(bins)-1):
        count = 0
        for value in values:
            if bins[i] <= value < bins[i+1]:
                count +=1
        numbr.append(count)
            
    

    plt.bar(range(len(bins)-1), numbr)
    plt.xlabel(att)
    plt.ylabel("Number of students")
    plt.show()
    
    return None

# Do NOT include a main script in your submission
