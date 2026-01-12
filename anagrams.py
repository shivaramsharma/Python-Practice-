#Check if two strings are anagrams of each other.
name1 = "shiva"
name2 = "ivash"

if (sorted(name1) == sorted(name2)):
    print("given strings are anagrams")
else:
    print("given strings are not anagrams")
