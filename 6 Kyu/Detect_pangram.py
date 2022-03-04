# Decription
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# Example
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. Ignore numbers and punctuation.

import string
s = "Aacdefghijklmnopqrstuvwxyz"
value = 0
for i in set(s.lower()):    #create a set of s, so any repeated letters are removed. Aa would be missed by set() hence .lower() ---> aa which means a is counted once.
    if i in string.ascii_letters: # if i is in the alphabet(string.ascii_letters). the counter value goes up by 1
        value += 1
#if all 26 characters in the aphabet are present, value should equal 26 hence the string is a pangram and should return True
if value == 26: 
    print(True)
else:
    print(False)
        

import string

def is_pangram(s):
    return 26 == sum(i in string.ascii_letters for i in set(s.lower()))  #comparing length of characters
    return set(string.lowercase) <= set(s.lower()) #comparing sets of characters


