'''NAME
       Euler
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Euler's method to predict the location of a point in a differential equation
CATEGORY
        Numeric methods
USAGE
        Euler.py
'''
#IMPORT LIBRARIES
from sympy import *

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x, y = symbols('x y')

print("\t\t-- Welcome to Euler's method --")

#GET THE EQUATION OF THE FUNCTION
equation = sympify((input('-> Insert the equation in terms of "x" and "y": ')).replace('e','E'))

#ASK FOR VALUES THAT WILL BE USED
h = N(input('-> Insert the value for h (difference between intervals): '))
xValue = N(input('-> Insert initial value for "x": '))
yValue = N(input(f'-> Insert value for "y" in y({xValue}): '))
xFinal = N(input('-> Insert final value for "x": '))

#START ITERATIONS UNTIL xValue INITIAL REACHES xFinal VALUE
if h > 0:
    while xValue <= round((xFinal-h),6):
        yValue = yValue + (h * N(equation.subs([(x, xValue),(y, yValue)])))
        xValue = round(xValue + h, 6)
else:
    while xValue >= round((xFinal-h),6):
        yValue = yValue + (h * N(equation.subs([(x, xValue),(y, yValue)])))
        xValue = round(xValue + h, 6)

#CHECK IF THE USER WANTS TO ROUND THE RESULT
if input('-> Would you like to round the result? (Y/N) --> ').upper() == 'Y':
    rounder = int(input('\tInsert the decimals to round for the result: '))
    print(f'\tThe solution is {round(yValue, rounder)}')
else:
    print(f'\tThe solution is {yValue}')
# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# x              string       Represents the symbol "x" that will be use in equations
# y              string       Represents the symbol "y" that will be use in equations
# equation       sympify      It stores the general equation
# h              float        Indicates the difference between each x in iterations
# xValue         float        Saves the x value for each iteration
# yValue         float        Saves the y value for each iteration
# xFinal         float        Saves the last value for x
# rounder        int          Indicates the number of decimals taht will be rounded
