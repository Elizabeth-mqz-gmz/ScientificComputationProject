'''NAME
       RungKutt
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Runge Kutta method to predict the location of a point in a differential equation
CATEGORY
        Numeric methods
USAGE
        RungKutt.py
'''
#IMPORT LIBRARIES
from sympy import *

def RungeKutta(yValue):
    #CREATE K VALUES
    kAbs = 0
    kList.clear()
    kList.append(h * N(function.subs([(x, xValue),(y, yValue)])))
    kList.append(h * N(function.subs([(x, xValue + (h/2)),(y, yValue + (kList[0]/2))])))
    kList.append(h * N(function.subs([(x, xValue + (h/2)),(y, yValue + (kList[1]/2))])))
    kList.append(h * N(function.subs([(x, xValue + h),(y, yValue + kList[2])])))

    #MODIFICATE SPECIAL CASES
    for i in range (0,4):
        if i == 1 or i == 2:
            kAbs += 2 * kList[i]
        else:
            kAbs += kList[i]

    yValue = yValue + ((1/6)*(kAbs))
    return yValue

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x, y = symbols('x y')

print('\t\t-- Welcome to Runge Kutta method --')

#GET THE EQUATION OF THE FUNCTION
function = sympify((input('-> Insert the equation in terms of "x" and "y": ')).replace('e','E'))

#GET VALUES THAT WILL BE USED
h = N(input('-> Insert the value for h (difference between intervals): '))
xValue = N(input('-> Insert initial value for "x": '))
yValue = N(input(f'-> Insert value for "y" in y({xValue}): '))
xFinal = N(input('-> Insert final value for "x": '))

#START ITERATIONS
kList = []
if h > 0:
    while xValue < xFinal:
        yValue = RungeKutta(yValue)
        xValue = xValue + h
else:
    while xValue >= round((xFinal-h),6):
        yValue = RungeKutta(yValue)
        xValue = xValue + h

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
# function       sympify      It stores the general equation
# h              float        Indicates the difference between each x in iterations
# xValue         float        Saves the x value for each iteration
# yValue         float        Saves the y value for each iteration
# xFinal         float        Saves the last value for x
# kList        list, float    This structure records the values of each k evaluated
# kAbs           float        Saves the accumulate sum of every k value
# i              int          Iterator variable
# rounder        int          Indicates the number of decimals that will be rounded
