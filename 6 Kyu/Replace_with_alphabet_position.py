# Description:
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
    new_str = list()
    new_text = text.lower()
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    #traverse through the text, if the element is in the dicitonary it gets replaced by the correspoding numeber
    for i in new_text:
        if i in dict:
            new_str.append(i.replace(i, dict[i]))
    #return the list of numbers into a string
    return " ".join(new_str)

def alphabet_position(text):

    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    return " ".join([i.replace(i, dict[i]) for i in text.lower() if i in dict])

#solution using ord from codewars solutions:
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

#solution using .index() from codewars solutions:
import string

def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower())+1) for letter in list(text) if letter.isalpha()])
    #instead of using a dictionary import the ascii letters from the module string.
    #replaces the letter for it's place in the index of the alphabet in the list of the text if the letter is in the alphabet.