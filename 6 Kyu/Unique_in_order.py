# Description:
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

# Example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    lst = []  #new list to hold the new sequence.
    prev = None  # no previous value to begin with therefore add use None
    for i in iterable:
        if i != prev: #prev = previous element in the sting or list. Checking the previous element to enture we are not adding a repeated element
            lst.append(i)
        prev = i # previous element is updated to the most recent element.
    return (lst)

#        if len(res) == 0 or item != res[-1]:  insttead of creating prev

