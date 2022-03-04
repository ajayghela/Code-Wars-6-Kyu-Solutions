# Description:
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed 
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    new_str = ""
    for word in sentence.split():
        if len(word) < 5:
            new_str += word + " "  #split the sentance, if the element is <5 characters long add word to new_str
        else:
            new_str += word[::-1] + " " #if the element is >5 characters long add the reveresed word to new_str
    return new_str.rstrip()

def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())
 
        

