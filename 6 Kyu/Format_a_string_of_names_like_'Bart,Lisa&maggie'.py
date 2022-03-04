# Description:
# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand.

# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    str = ''
    if len(names) != 0:
        lst = [names[i]['name'] for i in range(0, len(names) - 1)] #list of names not including the last name
        str = ', '.join(lst) #list is converted into string separted by commas
        str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name'] #if the string is not empty then add '&' and the last name in the list else just the last name (this covers the case in which there is only one name on the list) 
    return str

#alternative using format codewars best practices:
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''