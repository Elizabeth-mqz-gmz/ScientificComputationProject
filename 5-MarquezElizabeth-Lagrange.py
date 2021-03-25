'''NAME
       Lagrange
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of lagrange interpolation to construct a polynomial and find a solution for x
CATEGORY
        Numeric methods
USAGE
        Lagrange.py
'''
#IMPORT LIBRARIES
from sympy import *

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x = symbols('x')

print('\t\t-- Welcome to Lagrange interpolation method --')

#FUNCTION TO GET x AND y VALUES
def GetValues(axis):
    values = input('Insert '+ axis +' values, please separe them with a coma between each one\n')
    return values.split(',')

#GET x AND y VALUES
correct = False
while not correct:
    xAxis = GetValues('x')
    yAxis = GetValues('y')
    if len(xAxis) != len(yAxis):
        print('The number of elements for x axis is not the same for y axis.\nThe method requires same number of elements for both axis, insert again the values.')
    else:
        correct = True
#SAVE x AND y VALUES IN LISTS
xAxis = list(map(float, xAxis))
yAxis = list(map(float, yAxis))

n = len(xAxis)
sumEq = 0

#ITERATE TO CREATE THE POLYNOMIAL
for i in range(1,n+1):
    numEq = 1
    denominator = 1
    for j in range(1,n+1):
        if i == j:
            continue
        #CREATE EQUATION
        numEq = expand(numEq * (x - xAxis[j-1]))
        denominator = denominator * (xAxis[i-1] - xAxis[j-1])
    sumEq += expand(numEq/denominator) * yAxis[i-1]

print(f'\tA polynomial has been constructed:\t{sumEq}')

solveX = input('Would you like to solve for x? (Y/N) --> ').upper()
if solveX == 'Y':
    xValue = float(input('Insert the x value to evaluate: '))
    #EVALUATE WITH x VALUE
    print(f'\tx=\t{N(sumEq.subs(x, xValue))}')
# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# x              string       Represents the symbol "x" that will be use in equations
# correct        bool         Indicates if values inserted are coherent
# xAxis          list, float  Saves x values
# yAxis          list, float  Saves y values
# n              int          Indicates the number of elements to iterate
# i              int          Controls interations
# numEq          sympify      Saves temporal solutions
# denominator    float        Indicates denominator values
# j              int          Controls intern iteration
# sumEq          sympify      Saves polynomial
# solveX         string       Indicates if has been required a solve for x
# xValue         float        Saves the value for x that will be evaluated
#             +----GetValues----+
# *NAME*         *TYPE*        *USAGE*
# axis           string        Indicates the letter x o y
# values         string        Saves values
