#Using str.partition() and str.replace()

a = "Hello, how are you?"

words, rem = [], a
while rem:
    head, _, rem = rem.partition(" ")
    if head:
        words.append(head)

c = "-".join(words)
print(words)
print(c)