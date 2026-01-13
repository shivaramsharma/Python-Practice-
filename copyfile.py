#Create a program that copies the contents of one file into another

try:
    with open('interviews.txt','r') as file:
        lines = file.readlines()
    with open('interviews1.txt','w') as file_w:
        
        for line in lines:
            file_w.writelines(line)

except FileNotFoundError:
     print("Error: The file 'your_file.txt' was not found.")
