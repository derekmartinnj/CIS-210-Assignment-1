'''
P12 Intro
CIS 210 W19 Project 1

Author: Derek Martin

Credits: N/A

Implement several functions that perform various calculations
'''

def convert(i, j, k):
    '''
    (int) (int) (int) -> str

    Convert the three given ints into one that is structured based on the significance of each digit
    
    >>> convert(1, 2, 3)
    321
    >>> convert(0, 0, 1)
    100
    '''
    i = int(i)
    j = int(j)
    k = int(k)
    if (((i >= 0) and (i <= 9)) and ((j >= 0) and (j <= 9)) and ((k >= 0) and (k <= 9))):
        i = str(i)
        j = str(j)
        k = str(k)  #Convert to strings to allow concatenation
        converted = (k + j + i)
        converted = int(converted)  #Convert back to int to return a numeric value
        return converted

def add_digits(n):
    '''
    (int) -> int

    Input a 3 digit int and return the sum of each digit

    >>> add_digits(123)
    6
    >>> add_digits(101)
    2
    '''
    n = int(n)
    if ((n >= 100) and (n <= 999)):
        n = str(n)  #Convert to string to allow the separation of each digit
        firstdig = n[0]
        seconddig = n[1]
        thirddig = n[2]
        firstdig = int(firstdig)
        seconddig = int(seconddig)
        thirddig = int(thirddig)
        return (firstdig + seconddig + thirddig)

def profit(attend):
    '''
    (int) -> float

    Calculate the profit of a movie theatre based on the cost of each attendee

    >>> profit(5)
    2.5
    >>> profit(10)
    25.0
    '''
    attend = int(attend)
    gross = 5 * attend
    cost = 20 + (0.5 * attend)
    profit = gross - cost
    profit = float(profit)  #Convert to float to allow for more precise result
    return profit
