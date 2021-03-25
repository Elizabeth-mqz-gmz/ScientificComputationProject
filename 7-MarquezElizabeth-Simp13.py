'''NAME
       Simp13
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Simpson 1/3 method to find an area between the limits of a function
CATEGORY
        Numeric methods
USAGE
        Simp13.py
'''
#IMPORT LIBRARIES
from sympy import *

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x = symbols('x')

print('\t\t-- Welcome to Simpson 1/3 method --')

#GET THE EQUATION OF THE FUNCTION
equation = sympify((input('-> Insert the integrand in terms of "x": ')).replace('e','E'))

#ASK FOR LIMITS AND NUMBER OF BANDS
correct = False
inf = N(input('-> Insert lower limit for the integral: '))
sup = N(input('-> Insert superior limit for the integral: '))
while not correct:
    bands = int(input('-> Insert number of bands: '))
    correct = True if bands%2 == 0 else False

#DEFINE START VALUES
h = (sup-inf)/bands
y0 = N(equation.subs(x, inf))
yn = N(equation.subs(x, inf + (bands * h)))
sum = y0 + yn

#START THE CYCLE
for i in range(1, bands):
    if i%2 == 0:
        sum += 2 * N(equation.subs(x, inf + (i * h)))
    else:
        sum += 4 * N(equation.subs(x, inf + (i * h)))

sum *= h/3
#CHECK IF THE USER WANTS TO ROUND THE RESULT
if input('-> Would you like to round the result? (Y/N) --> ').upper() == 'Y':
    rounder = int(input('\tInsert the decimals to round for the result: '))
    print(f'\tThe value of area is {round(sum, rounder)}')
else:
    print(f'\tThe value of the area is {sum}')
# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# x              string       Represents the symbol "x" that will be use in equations
# equation       sympify      It stores the general equation
# sup            float        Indicates the superior value for the integrand
# inf            float        Indicates the lower value for the integrand
# bands          int          It stores the number od band in wich the area will be divided
# h              float        Indicates h value
# y0             float        Indicates the value of "y" evaluated at initial value of "x"
# yn             float        Indicates the last value of "y"
# sum            float        Accumulates the sum of values to get the area
# i              int          Iterator variable
# correct        boolean      Checks if something is allowed to the method
