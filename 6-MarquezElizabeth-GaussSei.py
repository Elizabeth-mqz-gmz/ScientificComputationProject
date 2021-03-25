'''NAME
       GaussSei
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Implementation of Gauss-Seidel method to find an intersection point
CATEGORY
        Numeric methods
USAGE
        GaussSei.py
'''
#IMPORT LIBRARIES
from sympy import *

def Sum(index, position):
    #GET THE SUM OF ELEMENTS THAT ARE NOT AT THE DIAGONAL
    sum = 0
    for num in range(0,numEquations):
        #!= TO DIAGONAL ELEMENTS AND RESULT OF EQUATION
        if num != position and num < numEquations:
            sum += equationsPackage[index][num]
    return abs(sum)

def Number(index, position):
    return equationsPackage[index][position]

equationsPackage = {}

print('\t\t-- Welcome to Gauss-Seidel method --')

numEquations = int(input('-> Insert the number of equations to evaluate: '))

#GET SYSTEM OF EQUATIONS
equation = 0
while equation < numEquations:
    values = input(f'Insert values for equation {equation+1}, please separe them with a coma between each one\n')
    values = list(map(float, values.split(',')))

    #CHECK IF NUMBER OF ELEMENTS IN EQUATIONS ARE THE EXPECTED
    if len(values) == (numEquations+1):
        equationsPackage.update({equation:values})
        equation += 1
    else:
        print('The expected values were not recived, please try again')

rounder = int(input('-> Give the number of decimals for the method precision: '))

#ACCOMMODATE THE SYSTEM TO BE DIAGONALLY DOMINANT
exc = 0
for k in range(0,numEquations):
    if exc == numEquations:
        break
    for i in range(0,numEquations):
        if abs(equationsPackage[k][i]) > Sum(k,i):
            exc += 1
            break
        for j in range(0,numEquations):
            if j < numEquations:
                if abs(equationsPackage[i][j]) > Sum(i,j):
                    #MAKE POSITION EXCHANGE OF EQUATIONS, j INDICATES THE POSITION FOR DIAGONAL
                    save = equationsPackage[j]
                    equationsPackage[j] = equationsPackage[i]
                    equationsPackage[i] = save
                    break
print('\t-Here is the system of equations diagonally dominant-')
for i in range(0,numEquations):
    for j in range(0,numEquations):
        print(equationsPackage[i][j], end = '\t')
    print(f'|\t{equationsPackage[i][j+1]}', end = '\n')
    
#ADD 0 THAT INDICATES THE INITIAL VALUE OF THE VARIABLE INSIDE THE EQUATION
for i in range(0, numEquations):
    equationsPackage[i].append(0)

#START ITERATIONS TO GET VALUES OF SOLVED EQUATIONS
converge = False
while not converge:
    counter = 0

    #LOOP THROUGH EACH EQUATION
    for m in range(0,numEquations):
        totalSum = 0
        for n in range(0,numEquations+1):
            #AVOID DIAGONAL VALUE, THIS WILL BE USED TO DIVIDE totalSum
            if n != m:
                if n == numEquations:
                    totalSum += Number(m,n)
                else:
                    totalSum += (-1*(Number(m,n)))*Number(n,numEquations+1)
        if Number(m,m) != 0:
            totalSum /= Number(m,m)

        #IF THE NEW VALUE EQUALS THE PREVIOUS VALUE, COUNTER WILL RECORD THE EQUATIONS THAT HAVE CONVERGED
        if round(totalSum, rounder) == round(Number(m, numEquations+1), rounder):
            counter += 1
        else:
            equationsPackage[m][numEquations+1] = totalSum

    #IF ALL EQUATIONS HAVE CONVERGED, THE METHOD STOPS
    if counter == numEquations:
        for i in range(0, numEquations):
            print(f'\tThe value of unknown {i+1} is: {round(Number(i, numEquations+1), rounder)}')
        converge = True

# ------VARIABLE'S DICTIONARY------
#                   +----Main----+
#     *NAME*           *TYPE*             *USAGE*
# equationsPackage   dictionary, float    It stores the system of equations
# numEquations       int                  Indicates number of equations inside the system
# equation           int                  Indicates the equation number inside the counter
# rounder            int                  Saves the number of decimals for precision
# values             list                 Temporal variable, saves values that will be used in the system of equations
# save               float                It stores temporary a value
# counter            int                  Indicates the number of equations that have been converge
# converge           boolean              Indicates of the method had finished
# totalSum           float                Accumulates temporary the sum of values that have been evaluated
# exc                 int                 Controls if the system is already diagonally dominant
# m,n,i,j,k           int                 Iterator variable

#                   +----Sum----+
#     *NAME*           *TYPE*             *USAGE*
# equationsPackage   dictionary, float    It stores the system of equations
# index              int                  Indicates the key inside the dictionary that corresponds to the equation to evaluate
# position           int                  Indicates the value that corresponds to the value in the diagonal, this will be not added to sum
# num                int                  Indicates the index of the list that corresponds to the value that will be evaluated
# sum                float                Accumulates the sum of values
# numEquations       int                  Indicates the maximum number inside the for
#                  +----Number----+
#     *NAME*           *TYPE*             *USAGE*
# index                int                Indicates the number of equation
# position             int                Indicates the equation's element
