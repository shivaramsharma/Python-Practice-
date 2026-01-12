#Count the number of vowels in a string.

name = "shivaramyuii"
count = 0
for n in name:
    if n in ['a','e','i','o','u']:
        count = count+1

print(count)