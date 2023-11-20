# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Minjun Kim"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101256887"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-147"

#==========================================#
# Place your curve_fit function after this line
import numpy as np

def curve_fit(data: list[dict], attribute: str, order: int) -> str:
    """
    This function fit a polynomial curve to the data and return a string representation of the equation."
    
    """
    averages = {}
    for d in data:
        value = d[attribute]
        if value not in averages:
            averages[value] = []
        averages[value].append(d['G_Avg'])

    x = []
    y = []
    for key in sorted(averages.keys()):
        x.append(key)
        y.append(np.mean(averages[key]))

    if order > len(x) - 1:
        coeffs = np.polyfit(x, y, len(x) - 1)
        equation = np.poly1d(coeffs)
    else:
        coeffs = np.polyfit(x, y, order)
        equation = np.poly1d(coeffs)
    
    equation_str = 'y = '
    for i in range(len(coeffs)):
        power = len(coeffs) - i - 1
        coefficient = coeffs[i]
        if power > 1:
            equation_str += '{:.2f}x^{} + '.format(coefficient, power)
        elif power == 1:
            equation_str += '{:.2f}x + '.format(coefficient)
        else:
            equation_str += '{:.2f}'.format(coefficient)

    return equation_str    
# Do NOT include a main script in your submission


# Do NOT include a main script in your submission
