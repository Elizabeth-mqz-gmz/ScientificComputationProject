'''NAME
       Romberg
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Romberg method to find an area between the limits of a function
CATEGORY
        Numeric methods
USAGE
        Romberg.py
'''

#IMPORT LIBRARIES
from sympy import *

#DEFINE SYMBOLS THAT WILL BE USE IN EQUATIONS
x = symbols('x')
#DEFINE GLOBAL DICTIONARY FOR I VALUES
iPackage = {}

def CreateI(coefficient, jValueI):
    #EACH COEFFICIENT HAS TO BE DIVIDED BY 2 TO GET THE FRACTION OF C AT THE FIRST I's
    coefficient /= 2
    #DEFINE nDenominator TO GET THE FRACTION AND COEFFICIENT FOR EXTRA I's
    nDenominator, firstI, secondI = 1, 0, 0
    #'FOR' GOES FROM 1 TO ITERATION-1, AND IT CORRESPONDS TO HOW MANY I ELEMENTS WILL BE CREATED BY FLOOR
    for i in range(1, iIteration):
        if i == 1:
            #iPackage{1:[coefficient*c*J]} CREATE NATURAL I's
            iPackage.update({iIteration-2:[(coefficient*c) * jValueI]})
        else:
            #iPackage[1][0] GET <-(left) I
            firstI = iPackage[iIteration-2][i-2]
            #iPackage[0][0] GET <-(left) ?(up) I
            secondI = iPackage[iIteration-3][i-2]
            #iPackage{1:[coefficient*c*J, (1/3)*((4*[1][0])-[0][0])]} ADD EXTRA I's
            iPackage[iIteration-2].append((1/(nDenominator-1))*((nDenominator*firstI)-secondI))

        nDenominator *= 4
    #TO KNOW WHICH IS THE FRACTION FOR NEXT ITERATION
    return coefficient

def CreateJ(previousJ, function):
    #powFraction IS THE KEY VALUE TO CREATE N TERMS FOR EACH FLOOR
    powFraction = 2**(iteration)
    numerator = 1
    sumJ = 0
    #SPECIAL CASE
    if iteration == 0:
        jValue = (1/2)*(N(function.subs(x,inf))+N(function.subs(x,sup)))
    #FROM ITERATION 2 TO N THERE IS A PATRON IN WHICH J = previousJ + SUM OF powFraction/2 TERMS
    else:
        sumJ = previousJ
        for j in range(0,int(powFraction/2)):
            sumJ += N(function.subs(x,(inf+(numerator/powFraction)*c)))
            numerator += 2
        jValue = sumJ

    return jValue


print('\t\t-- Welcome to Romberg integration method --')

#GET THE ORIGINAL EQUATION OF THE FUNCTION
equation = sympify((input('-> Insert the equation in terms of "x": ')).replace('e','E'))

#CHECK RANGE VALUES
interval = False
while not interval:
    inf = N(input('-> Insert lower range value: '))
    sup = N(input('-> Insert superior range value: '))
    if sup > inf:
        interval = True

rounder = int(input('-> Give the number of decimals for the method precision: '))

converge = False
iteration = 0
iCoefficient = 2
c = sup - inf
iIteration = 2
jPrevious = 0

while not converge:
    jVal = CreateJ(jPrevious, equation)
    iCoefficient = CreateI(iCoefficient, jVal)

    if iteration > 0:
        #COMPARATE EACH I VALUE BY FLOOR TO LOOK FOR COINCIDENCE
        for index in range(0,len(iPackage[iteration])-1):
            if round(iPackage[iteration][index], rounder) == round(iPackage[iteration][index+1], rounder):
                root = round(iPackage[iteration][index+1], rounder)
                print(f'\tThe value of the area is: : {root}')
                converge = True
                break

    jPrevious = jVal
    iIteration += 1
    iteration += 1


# ------VARIABLE'S DICTIONARY------
#             +----Main----+
# *NAME*         *TYPE*        *USAGE*
# iPackage       dictionary   It stores the I values generated
# x              string       Represents the symbol "x" that will be use in equations
# equation       sympify      It stores the general equation
# rounder        int          Saves the number of decimals for precision
# interval       boolean      Serves to check if range values are coherent
# sup            float        Greater value of the range
# inf            float        Smallest value of the range
# converge       boolean      Serves to check if root has been found
# iteration      int          Controls the iteration number
# iCoefficient   float        Indicates the fraction value for c in natural I values
# c              float        Is the difference between greater and smallest range values
# iIteration     int          Controls an special iteration number for creation of I values
# jPrevious      float        It stores the last J value
# jVal           float        It stores the new J value
# index          int          Indicates the index in list of I values that are being compared
# root           float        Saves the root value

#             +----CreateI----+
# *NAME*         *TYPE*        *USAGE*
# coefficient     float        Indicates the fraction value for c in natural I values
# jValueI         float        It stores the J value that will be used for I natural calculation
# nDenominator    int          Number that indicates coefficient and denominator number for fractions in extra I's
# firstI          float        Saves previous I of the same floor for calculations of extra I
# secondI         float        Saves previous I of the previous floor for calculations of extra I
# i               int          Controls the number of iterations for creation of extra I's

#             +----CreateJ----+
# *NAME*         *TYPE*        *USAGE*
# previousJ      float        It stores the last J value
# function       sympify      It stores the general equation
# powFraction    int          Is the key value to create n terms for each floor
# numerator      int          Indicates numerator number
# sumJ           float        It stores sum of J values by each iteration
# jValue         floar        Saves the final value of J
# j              int          Controls the number of iterations for creation of terms that will accumulate for J total value
