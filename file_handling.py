import json 
import re

# with open('file.json','w') as file:
#     data = {"name": "Alice", "age": 25}
#     json.dump(data,file)
    

# with open('file.json','r') as file:
#     data = json.load(file)
#     print(data)

# with open('file.txt','a') as file:
#     file.write('welcome to new file\n')
#     file.write('second line\n')
#     file.write('third line\n')

# with open('file.txt','r') as file:
#     data = file.read()
#     search = re.compile('second')
#     match = search.findall(data)
#     print(match)



# list_var = [i for i in range(100)]
# sqre_list = map(lambda x:x**2,list_var)
# print(list(sqre_list))
# filter_list = filter(lambda x:(x%2==0),list_var)
# print(list(filter_list))
# def bubble_sort(array):
#   """Sorts the given array in ascending order using the bubble sort algorithm.

#   Args:
#     array: A list of elements to be sorted.

#   Returns:
#     A sorted list.
#   """

#   for i in range(len(array) - 1):
#     for j in range(len(array) - i - 1):
#       if array[j] > array[j + 1]:
#         array[j], array[j + 1] = array[j + 1], array[j]

#   return array

# li = [4,3,5,6,1]
# li_new = bubble_sort(li)

# print(li_new)

def decorator(func):
    def multiplier(x):
        result = func(x)
        return result+2
    return multiplier

@decorator
def func(x):
    return x*x

print(func(2))
print(decorator(2))
var_x = set([1,2,3,4,5,6])
var_x.add(7)
print(var_x[3])
