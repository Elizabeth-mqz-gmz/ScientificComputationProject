'''NAME
       numerical_methods_lib
VERSION
        1.0
AUTHOR
        Elizabeth Marquez Gomez <elimqzg@lcg.unam.mx>
DESCRIPTION
        Library to find x0 value and to get the root of a function using Successive Approximations method and Newton Raphson method
CATEGORY
        Numeric methods
USAGE
        from numerical_methods_package import numerical_methods_lib
'''
#IMPORT LIBRARIES
from sympy import *

x = symbols('x')

#FIND SIGN CHANGE
def FindSignChange(equation, inf, sup, add):

    iInf,iSup = 0,0
    resultsPackage = {}
    print('\t---  Tabulation  ---\n\tX\t\tY')
    previous, index, change = 0, 0, 0
    #START AND SAVE TABULATIONS, DETECT IF THERE ARE SOME SIGN CHANGES
    while inf <= sup:
        print(f'\t{inf}\t{N(equation.subs(x, inf))}')
        resultsPackage.update({index:(inf, N(equation.subs(x, inf)))})
        if previous * N(equation.subs(x, inf)) < 0:
            change += 1
        previous = N(equation.subs(x, inf))
        index += 1
        inf += add

    if change == 0:
        #REFINE INTERVAL
        if add >= 0.1:
            add /= 2
            print(f'\tWe could not find an aproximation of the root inside the interval.\n\tWe will refine the interval, the step is now {add}')
            FindSignChange(equation, inf, sup, add)
        else:
            print('\tIs not possible to find a root in the interval')
            exit()

    print('We have detected possible values for x0 in these intervals:')
    option = 1
    optionsList = []
    intervalOptionList = []
    #SHOW APPROXIMATIONS TO ROOTS INSIDE THE FUNCTION, GIVE OPTIONS TO USER
    for i in range(0,len(resultsPackage)-1):
        if resultsPackage[i][1] * resultsPackage[i+1][1] < 0:
            iInf, iSup = resultsPackage[i][0], resultsPackage[i+1][0]

            print(f'Option {option}')
            print(f'\tX\t|\tY')
            print(f'\t{iInf}\t|\t{resultsPackage[i][1]}\n\t{iSup}\t|\t{resultsPackage[i+1][1]}')

            value = (iInf+iSup)/2
            intervalOptionList.append((iInf, iSup))
            optionsList.append(value)
            option += 1
    #GET THE OPTION AND SAVE APPROXIMATION
    option = int(input('-> Type the number of the option that you want to use for "x0": '))
    x0 = optionsList[option-1]
    iInf, iSup = intervalOptionList[option-1][0], intervalOptionList[option-1][1]
    print(f'The selected value for "x0" is: {x0}')

    return [x0, iInf, iSup]

def MethodFind(xValue, previous, rounder, iteration, expression, max, method):
    if iteration < max:
        iteration += 1

        #SuccessiveApproximations
        if method == 0:
            result = N(expression.subs(x,xValue))
        #NewtonRaphson
        if method == 1:
            result = xValue - (N(expression[0].subs(x, xValue))/N(expression[1].subs(x, xValue)))

        print(f'\t   {iteration}\t     {result}')

        if round(result, rounder) == round(previous, rounder):
            res = round(result, rounder)
            print(f' The method have found the root: : {res}\n Iterations made: {iteration}')
            return
        else:
            res = MethodFind(result, result, rounder, iteration, expression, max, method)
            return res

    else:
        print(f' The number of iterations has been exceeded.\n The found root is {xValue} in {iteration} iterations.')
        return
#             +----FindSignChange----+
# *NAME*                *TYPE*        *USAGE*
# equation              sympify       It represents the equation to use
# inf                   float         Indicates the lower value for the range
# sup                   float         Indicates the upper value for the range
# add                   float         Indicates the addition for each tabulation
# iInf                  float         Saves the lower value for range
# iSup                  float         Saves the upper value for range
# resultsPackage      dictionary      It stores ranges of posible values for x0
# previous              float         Saves the previous value of the iteration to check if there is a sign change
# index                 int           Indicates an index to save possible x0 values
# change                int           Indicates how many sign changes could exist
# option                int           Indicates the option to take x0 value
# optionsList           list          Saves the possible values for x0
# intervalOptionList    list          Saves the interval values for possible x0
# i                     int           Controls the iterations inside the for
# value                 float         Saves temporary values for x0
# x0                    float         Indicates the selected value for x0
#               +----MethodFind----+
# *NAME*         *TYPE*        *USAGE*
# iteration       int          It stores the counter of iterations
# xValue          float        Indicates the x value that will be used to evaluate
# previous        float        Is the x value to compare if there is converge
# rounder         int          Indicates the number of decimals to round
# iteration       int          Saves the number of iteration
# expression     sympify       It indicates the equation to use
# max             int          Indicates the maximum number of iterations to do
# method          int          Indicates the method to use
# result          float        Saves the result of iteration to compare
# res             float        Saves the final result for the root
