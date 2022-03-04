# Description   
# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. 
# The first word within the output should be capitalized 
# only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if len(text) == 0: 
        return ''
    text_conv1 = text.replace('_', ' ').replace('-', ' ')
    camel_case = "".join(word.capitalize() for word in text_conv1.split())
    return text_conv1[0] + camel_case[1:]

def to_camel_case(text):
    camel_case = "".join(word.capitalize() for word in text.replace('_', ' ').replace('-', ' ').split()) # create new string where each word is capitalised in the text string after _ and - have been replaced and split.
    if len(text) == 0: 
        return '' 
    else:
        #the original first letter in the string enures the first letter is capitalised only if it was orginally capitalised then adds the new string. 
        return text[0] + camel_case[1:] 
    
