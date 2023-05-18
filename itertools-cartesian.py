################
#
# using custom function
#

list_a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
list_b = [1,0]

def cartesian_product(list1, list2):
        
    list1 = sorted([int(x) for x in list1 if x != ' '])
    list2 = sorted([int(x) for x in list2 if x != ' '])
    final_list = []
    
        
    if len(list1) and len(list2) < 30:
        if len(list1) and len(list2) > 0:
    
            for index, x in enumerate(list1):
                for value in list2:
                    final_list.append((x, value ))
            
            final_list.sort(key=lambda a: a[1])
    
            output = ' '.join(str(x) for x in final_list)
            print(output)
            
cartesian_product(list_a, list_b)


################
#
# using product module
#

from itertools import product

list_a = [int(x) for x in list_a if x != ' ']
list_b = [int(x) for x in list_b if x != ' ']

result = list(product(list_a, list_b))
result.sort(key=lambda a: a[1])

output = ''

for index, x in enumerate(result):
    
    if index == len(result) - 1:
        output += str(x)
        break
    
    output += str(x) + ' '

print(output)

