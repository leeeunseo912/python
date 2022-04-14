list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy() 

list2[0][1] = 'c'
list2[1] = 1000

print(list1)
print(list2)