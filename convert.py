#Convert Snake case to Pascal case

a = "ShIvAraM RamaRao SandEp"
res = ''.join(word.capitalize() for word in a.split(" "))
print(res)