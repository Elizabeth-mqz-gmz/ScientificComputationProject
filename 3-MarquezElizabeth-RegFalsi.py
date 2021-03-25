'''NAME
       RegFalsi
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Regula Falsi method to find a root in a function
CATEGORY
        Numeric methods
USAGE
        RegFalsi.py
'''
#IMPORT LIBRARIES
from sympy import *
from numerical_methods_package import numerical_methods_lib

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x, xn, k = symbols('x xn k')

print('\t\t-- Welcome to Regula Falsi method --')

#GET THE ORIGINAL EQUATION OF THE FUNCTION
equation = sympify((input('-> Insert the equation in terms of "x": ')).replace('e','E'))

#GET THE NUMBER NERBY TO THE ROOT SO IT CAN START ITERATIONS
interval = input('\tWe will show an interval between -10 and 10, if you want to use it press 0.\n\tOtherwise if you want to see tabulations for an specific interval, please insert it separated by commas: ')
add = float(input('-> Insert the addition for each tabulation: '))
if interval == '0':
    x0Value = numerical_methods_lib.FindSignChange(equation, -10, 10, add)
else:
    valuesCorrect = False
    while not valuesCorrect:
        interval = interval.split(',')
        if float(interval[0]) < float(interval[1]):
            valuesCorrect = True
        else:
            interval = input('\t-> Insert the intervals separated by commas: ')

    x0Value = numerical_methods_lib.FindSignChange(equation, float(interval[0]), float(interval[1]), add)

maxIterations = int(input('-> How many iterations should the method do?: '))
rounder = int(input('-> Give the number of decimals for the method precision: '))

#CREATE FUNCTION REGULA FALSI TO USE IT EASIER DURING ITERATIONS
functionRF = sympify((xn*N(equation.subs(x, k))-k*N(equation.subs(x, xn)))/(N(equation.subs(x, k))-N(equation.subs(x, xn))))
converge = False
iteration = 0
a = x0Value[1]
b = x0Value[2]

#DEFINE K VALUE
xValue = ((a*N(equation.subs(x, b)))-(b*N(equation.subs(x, a))))/(N(equation.subs(x, b))-N(equation.subs(x, a)))
kValue = b if N(equation.subs(x, xValue)) * N(equation.subs(x, b)) < 0 else a

print('\t-- x --    |    -- Root --')
print(f'\t   {0}\t     {xValue}')

while not converge:

    if iteration >= maxIterations:
        print(f' The number of iterations has been exceeded.\n The found root is {result} in {iteration} iterations.')
        break
    else:
        iteration += 1
        result = N(functionRF.subs([(xn,xValue),(k,kValue)]))
        print(f'\t   {iteration}\t     {result}')

        #CHECK IF IT'S NEEDED A CHANGE OF K VALUE
        if N(equation.subs(x, xValue)) * N(equation.subs(x, result)) < 0:
            kValue = N(equation.subs(x, xValue))

        if round(result, rounder) == round(xValue, rounder):
            result = round(result, rounder)
            print(f' The method have found the root: : {result}\n Iterations made: {iteration}')
            converge = True
        else:
            xValue = result

# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# x              string       Represents the symbol "x" that will be use in equations
# xn             string       Represents the symbol "xn" that will be use in equations
# k              string       Represents the symbol "k" that will be use in equations
# equation       sympify      It stores the general equation
# functionRF     sympify      It stores the regula falsi general equation
# maxIterations  int          Saves the maximum number of iterations
# converge       bool         Indicates if converge has been obtained
# rounder        int          Saves the number of decimals for precision
# a              float        Greater value of the range
# b              float        Smallest value of the range
# iteration      int          Indicates the iteration number
# xValue         float        Saves the value of x by iteration
# kValue         float        Saves pivot value
# result         float        Saves the new x value
# interval         int          Indicates the interval to use for tabulations
# add              float        Indicates the addition for each tabulation
# valuesCorrect    bool         Indicates if values of range are coherent
# x0Value      float, list    First stores the x0 value, and then stores a list with superior, lower and x0 values
