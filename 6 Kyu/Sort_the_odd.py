# Description
# You will be given an array of numbers. You have to sort the odd numbers in ascending order 
# while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

sort_array = [5, 3, 2, 8, 1, 4]
# original_array = enumerate(sort_array)
# order_array = sorted(sort_array)
# final = list()
# for count,value in original_array:
#     if value%2 != 0:
#         final.append(order_array[count])
#     else:
#         final.append(sort_array)

odd = sorted([i for i in sort_array if i%2 !=0])
c = 0
final = []
for i in sort_array:  #creating a new list of numbers
    if i%2 !=0:       #  if the value in the array is odd
        final.append(odd[c])   # this value gets replaced by the value in odd in the place denoted by c
        c += 1          # the count c is increased by 1 so the next odd number is picked when looped though again.
    else:                        
        final.append(i)            

def sort_array(source_array):
    odd = iter(sorted([i for i in source_array if i%2 != 0]))  # iter makes the sorted list iterable
    return [next(odd) if i%2 !=0 else i for i in source_array] #final list with next(odd) calls the next element in the list of i.

