''' 
CIS 210 STYLE
CIS 210 W19 Project 1-1

Author: Derek Martin

Credits: N/A

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''(bool, bool) -> str

    Return specific string based on the value of (onTime) and (absent) variables.
    
    >>> q1(True, False)
    Hello!
    >>> q1(False, False)
    Better late than never.
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''(int, int) -> bool

    Return (True) or (False) based on the value of (age) and (salary) variables, and how these values fit into the specified conditional statement.
    
    >>> q2(20, 50000)
    False
    >>> q1(16, 8000)
    True
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''() -> int

    Based on specified conditional statements and the math that is implemented with them, return the value of (result)
    
    >>> q3()
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''(float, float) -> float

    Iterate through a while loop that adds (deposit) to the value of (balance). Return the balance 
    
    >>> q4(100.0, 50.0)
    600.0
    >>> q4(300.0, 40.0)
    700.0
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''(list) -> int

    Return value of (result) after iterating through the given while loop and implementing the math.
    
    >>> q5([1, 2, 3, 4])
    4
    >>> q5([5, 6, 7, 8])
    4
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''() -> int

    Returns value of p after iterating through the given while loop and implementing the math.
    
    >>> q6()
    16
    '''
    i = 0
    p = 1
    while i < 4:
        p = p * 2
        i += 1 #safely increment (i) to avoid infinite loop)

    return p
