'''                          # FILE HEADER
Nature's Thermometer: Cricket Chirps.
CIS 210 W19 Project 1

Author: Derek Martin

Credits: N/A

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''

def chirps_to_ctemp(ch25):  
    '''(int) -> float       
                            
    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temperature.
                           
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''
    ctemp = 0.0
    ctemp = (ch25 / 3) + 4
    return round(ctemp, 1) #round to nearest tenth to be precise, because of celsius result


def chirps_to_ftemp(ch14):
    '''(int) -> int

    Return fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40. 

    >>> chirps_to_ftemp(0)
    40
    >>> chirps_to_ftemp(50)
    90
    '''    
    ftemp = 0
    ftemp = ch14 + 40
    return ftemp
