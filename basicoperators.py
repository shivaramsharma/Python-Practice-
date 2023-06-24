#arthemeticoperators

number = 1 + 2 * 3 / 4.0
print(number)

remainder =  11 % 3
print(remainder)

squared =  7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#operators with strings

helloworld = "hello" +  " " + "world"
print(helloworld)

#multiplying string 

lotsofhello  = "hello" * 10
print(lotsofhello)

#operatorswithlists

evennumbers = [2,4,6,8]
oddnumbers = [1,3,5,7,9]
allnumbers = evennumbers + oddnumbers
print(allnumbers)

print([1,2,3] * 4)


#Excercise

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
biglist =  x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("biglist contains %d objects" % len(biglist))

if x_list.count(x) == 10 and y_list.count(y):
    print("Almost there")
if biglist.count(x) == 10 and biglist.count(y):
    print("Great")    