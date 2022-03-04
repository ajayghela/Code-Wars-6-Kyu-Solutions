# Description
# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

# Examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.


def likes(name):
    while len(name) >=0:        #open a loop to go through the array
        if len(name) == 0:
            return "no one likes this"   #instructions for if len of array is 0
        elif len(name) == 1:
            return name[0] + ' likes this' #instructions for 1 like
        elif len(name)== 2:
            return name[0] + " and " + name[1] + ' like this' #instructions for 2 likes
        elif len(name) == 3:
            return name[0] + ", " + name[1] + " and " + name[2] + ' like this'  #instructions for 3 likes 

        elif len(name) >= 4:
            num = str(len(name)-2)
            return name[0] + ", " + name[1] + " and " + num + " others like this"  #instructions for 4 or more people
        break
    

#ChiaraBells on the codewars website answer:
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

# anter69:
def likes(names):
    total = len(names)
    return ( 'no one likes this' if total == 0 else
             '%s likes this' % names[0] if total == 1 else
             '%s and %s like this' % (names[0], names[1]) if total == 2 else
             '%s, %s and %s like this' % (names[0], names[1], names[2]) if total == 3 else
             '%s, %s and %s others like this' % (names[0], names[1], total-2) )