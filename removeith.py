#How to Remove Letters From a String in Python

a = "hello world"
b = ""
remove_letter = "l"

for i in a:
    if i != remove_letter:
        b = b+i

print(b)
        


