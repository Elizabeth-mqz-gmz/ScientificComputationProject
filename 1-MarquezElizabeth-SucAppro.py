'''NAME
       SucAppro
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of successive approximations method to find a root in a function
CATEGORY
        Numeric methods
USAGE
        SucAppro.py
'''
#IMPORT LIBRARIES
from sympy import *
from numerical_methods_package import numerical_methods_lib

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x = symbols('x')

print('\t\t-- Welcome to successive approximations method --')

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


#GET THE DESPEJADA EQUATION OF THE FUNCTION
desp = sympify((input('-> Enter clearance of the equation in terms of "x": ')).replace('e','E'))

#DERIVING THE CLEAR OF THE EQUATION FOR THE CONVERGENCE CRITERIA
equationDiff = Derivative(desp, x)
equationDiff = equationDiff.doit()

x1 = N(desp.subs(x,x0Value[0]))
previousDifference = abs(x0Value[0]-x1)
if previousDifference >= abs(x1 - N(desp.subs(x,x1))):

    if N(equationDiff.subs(x, x0Value[0])) < 1:
      maxIterations = int(input('-> How many iterations should the method do?: '))
      rounder = int(input('-> Give the number of decimals for the method precision: '))
      print('\t-- x --    |    -- Root --')
      print(f'\t   {0}\t     {x0Value[0]}')
      #CALL TO SuccessiveApproximations METHOD TO GET THE ROOT VALUE OF THE FUNCTION
      numerical_methods_lib.MethodFind(x0Value[0], x0Value[0], rounder, 0, desp, maxIterations, 0)

    else:
      print('\tWe cannot find a root with the inserted equation, please try again with a different equation')

else:
    print(f'There is no converge with this equation')
# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# x              string       Represents the symbol "x" that will be use in equations
# equation       sympify      It stores the general equation
# x0Value        float, list  First stores the x0 value, and then stores a list with superior, lower and x0 values
# desp           sympify      It stores the clear equation
# maxIterations  int          Saves the maximum number of iterations
# equationDiff   derivative   It stores the derivative equation of the clear equation
# rounder        int          Saves the number of decimals for precision
# x1             float        Saves the first iteration
# previousDifference  float   Saves the difference between x0 and x1
# interval         int          Indicates the interval to use for tabulations
# add              float        Indicates the addition for each tabulation
# valuesCorrect    bool         Indicates if values of range are coherent
