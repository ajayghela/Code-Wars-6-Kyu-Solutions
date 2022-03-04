# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

#Iterate through the array 
# Count how many times a number occurs
# return the number if count is odd.
# Either by creating a dictionary or using the count method

def find_it(seq):
    new = dict()
    for i in seq:
        new[i]= new.get(i,0) + 1
    for k,v in new.items():
        if (v % 2) != 0: 
            return k

def find_it(s):
    for i in s:
        if s.count(i)%2!=0:
            return i

