#Words Frequency in String Shorthands

string1 = "hello world hello everyone"
res = {}
for word in string1.split():
    res[word] = res.get(word, 0) + 1
print(res)

    