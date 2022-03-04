# Description
# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then 
# it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

s = 'abc'
if (len(s)/2) % 2 != 0:
    s = s + '_'
new_str = []
n = 2
print([s[i : i + n]for i in range(0, len(s), n)])
   


