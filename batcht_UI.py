# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "George Grivas"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101273448"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-147"

#==========================================#
# Place your script for your batch_UI after this line
import load_data
import sort
import curve_fit
import histogram

def load(filename: str, col: str, fliter) -> list[dict]:
    try:
        file = open(filename)
        file.close()
    except:
        print("File not found.")

    data = load_data.add_average(load_data.load_data(filename, (col, fliter)))
    if data == []:
        print('Data loaded is empty.')
    else:
        print("Data loaded.")
    return data

def batcht_UI(cmdfile):    
    openfile = open(cmdfile, "r")
    data = []
    for line in openfile:
        info = line.strip().split(';')
        

        if info[0].upper() == 'L':
            data = load(info[1], info[2], info[3])

        elif info[0].upper() == 'S':
            if len(data) != 0:
            
                data = sort.sort(data, info[2], info[1])

                if info[3].upper() == 'Y':
                    print(data)
            else:
                print("File not loaded. Please, load a file first.")

        elif info[0].upper() == 'C':
            if len(data) != 0:

                print(curve_fit.curve_fit(data, info[1], int(info[2])))
            else:
                print("File not loaded. Please, load a file first.")


        elif info[0].upper() == 'H':
            if len(data) != 0:
                histogram.histogram(data, info[1])
                
            else:
                print("File not loaded. Please, load a file first.")


        elif info[1].upper() == 'E':
            break


        else:
            print("Invalid command")



