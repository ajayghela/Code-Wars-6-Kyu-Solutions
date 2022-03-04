#Description:
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters 
# and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) 
# and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# def duplicate_count(text):
 
def duplicate_count(text):
    letter_dict = dict() # Create a dictionary to count the number of times the characters occur
    for i in text.lower():
            letter_dict[i] = letter_dict.get(i,0) + 1 # adds i as the key and the value being the count

    count = 0 
    for k,v in letter_dict.items():
        if v > 1:
            count += 1
    return count

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1]) #the length of the list of the characters that occur more than once

def duplicate_count(text):
    count = 0
    # use set to get the individual characters that occur in the set (removes the duplicates)
    for c in set(text.lower()): 
        if text.lower().count(c) > 1: # if the count of c in text is more than one. 
            count += 1 #one is added to the counter
    return count #return count



