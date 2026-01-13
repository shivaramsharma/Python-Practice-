#Write a program to count how many times each word appears in a text file

with open('interviews.txt','r') as file_r:
    lines = file_r.readlines()

    for line in lines:
        print(line.split(" "))

