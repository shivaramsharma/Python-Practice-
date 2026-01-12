#Write a program to flatten a nested list
list1 = [[1,2],[3,4],[5,[6,7]]] 
list2 = []
list3 = []

for sublist in list1:
    list2.extend(sublist)

print(list2)

