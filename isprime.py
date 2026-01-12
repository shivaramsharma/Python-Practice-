#- Write a program to check if a number is prime.
num = 18
count = 0
for n in range(1,num):
    if num%n == 0:
        count = count + 1
    
if (count == 1):
    print("number is prime")
else:
    print("number is not prime")

    

