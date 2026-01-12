#Print all even numbers between 1 and 50.
count = 0
for i in range(1,500):
    for j in range(1,50):
        if(i%j == 0):
            count = count+1
    if(count == 2):
        print(i)
    count = 0
    