#- Find the largest and smallest number in a list.

list1 = [100,20,787,9,111]

max_number = list1[0]
min_number = list1[0]

for num in list1:
    if num > max_number:
        max_number = num
    elif num < min_number:
        min_number = num

print(max_number)
print(min_number)
