# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.


# iterate though the elements in the range of the number 
# Add the elements to a list and return the sum of that list if the modulus is 0


def solution(n):
    multiples = []
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            multiples.append(i)
    return sum(multiples)

def solution(n):
    return sum(i for i in range(n) if i%3 == 0 or i%5 == 0)
