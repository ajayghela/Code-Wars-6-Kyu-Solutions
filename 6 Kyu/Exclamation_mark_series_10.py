# # Description:
# Remove the minimum number of exclamation marks from the start/end of each word in the sentence to make their amount equal on both sides.

# Notes:
# Words are separated with spaces
# Each word will include at least 1 letter
# There will be no exclamation marks in the middle of a word
# Examples
# remove("Hi!") === "Hi"
# remove("!Hi! Hi!") === "!Hi! Hi"
# remove("!!Hi! !Hi!!") === "!Hi! !Hi!"
# remove("!!!!Hi!! !!!!Hi !Hi!!!") === "!!Hi!! Hi !Hi!"

# split into elements
# split each element again
# count the elements on each side 
# The lowest number of exclamations marks should be 
# 
import re
s = "!!!!Hi!! !!!!Hi !Hi!!!"
str = s.split()
for i,c in enumerate(str):
    before = 0
    after = 0
    while c[0] == '!':  #while the first character in the string is an "!"
        before += 1     #count + 1
        c = c[1:]       #the character, if a '!', is removed and the loop runs until the first character is not a '!'
    while c[-1] == '!': #while the last character in the string is an "!"
        after += 1      #count + 1
        c = c[:-1]      #the character, if a '!', is removed and the loop runs until the first character is not a '!'
    #the number of exclamation points should equall the smallest count
    count = min(before, after) 
    exc  = '!' *  count
    str[i] = exc + c + exc  #new string with the new amount of '!' on each side of c which is the string without an exclamation points
return " ".join(str)


