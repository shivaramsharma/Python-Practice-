#Find words which are greater than given length k

str = "hello geeks for geeks is computer science the portal" 
k = 5
words = str.split(" ")
str1 = ""
for word in words:
    if len(word) >= k:
        str1 = str1 + word + " "

print(str1)

