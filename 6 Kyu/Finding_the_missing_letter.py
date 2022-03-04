# Description
# Write a method that takes an array of consecutive (increasing) letters
# as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing. 
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:
# ['a','b','c','d','f'] -> 'e' 
# ['O','Q','R','S'] -> 'P'

# (Use the English alphabet with 26 letters!)

#convert chars into index
#create a set of characters that should match
import string
chars = ['O','Q','R','S']
#index of letters in alphabet
if chars[0] == chars[0].upper():
    index = dict(enumerate(string.ascii_uppercase)) 
else:
    index = dict(enumerate(string.ascii_lowercase))

chars1 = [k for k,v in index.items() for i in chars if i in v]
# chars1 range
conv_ = [k for k,v in index.items() if k in range(chars1[0], chars1[-1] + 1)]
#index of missing character
fin = list(set(conv_) - set(chars1))
print(index[fin[0]])




import string
def find_missing_letter(chars):
    #index of letters in alphabet
    index = dict(enumerate(string.ascii_letters)) 
    # part of the index that chars correponds with
    chars1 = [k for k,v in index.items() for i in chars if i in v]
    #part of the index that the list of letters should belong to.
    conv_ = [k for k,v in index.items() if k in range(chars1[0], chars1[-1] + 1)]
    #index of missing character
    fin = list(set(conv_) - set(chars1))
    return index[fin[0]]

import string
def find_missing_letter(chars):
    alphabet = list(string.ascii_letters)
    start = alphabet.index(chars[0])
    for i in range(len(chars)):
        if not chars[i] == alphabet[start+i]:
            return alphabet[start+i]