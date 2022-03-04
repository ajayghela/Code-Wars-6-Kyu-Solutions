# Description
# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    keys = [i for i in sentence if i.isdigit()] # creates a list based on the number in each word [2,1,4,3]
    values = [i for i in sentence.split()] # create a list of the words [is2, Thi1s, T4est, 3a]
    s_dict = dict(zip(keys,values)) # turn the lists to a dictionary where each number matches the word 
    sorted_keys = dict(sorted(s_dict.items())) #rearranges the order of the keys, lowest to highest, 
    return(" ".join(v for k,v in sorted_keys.items()))


def comp(x):
  for i in x:
      if i.isdigit():
          return int(i)
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=comp))

def order(s):
    new_order = []
    for num in range(1,10): # go thorugh the numbers in the range
        for word in list(s.split()): # split the sentence, turned into list. for each word in the list...
            if str(num) in word:    # if the number is in the word, that word will be added to the list
               new_order.append(word) # the word containing 1 is added first then the word containing 2 etc. 
    return " ".join(new_order) # list turned into a stirng.

