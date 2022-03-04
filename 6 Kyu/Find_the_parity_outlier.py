# Desciption:
# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
#  The array is either entirely comprised of odd integers or  entirely comprised of even integers except for a single integer N. 
#  Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

    
def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i%2 != 0:
            odd.append(i)  # creates list of odd integers
        else:
            even.append(i) # creates  list of even intergers
    if len(odd) < len(even):    # return the first value of smaller list which should contain the outlier 
        return odd[0]
    else:
        return even[0]   

def find_outlier(integers):
    odd = [i for i in integers if i%2 != 0]
    even = [i for i in integers if i%2 == 0]
    return odd[0] if len(odd)<len(even) else even[0]

    
