#list are nothing but array, here we have created array and appeneded 3 elements

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[2])
print(mylist[1])
#print(mylist[10]) --- index out of range
for x in mylist:
    print(x)

#examples of lists

numbers = [1,2,3]
names = ["hello", "world"]

second_name = "Eric"

print(numbers)
print(names)
print("second name is %s" % second_name)