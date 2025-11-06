# Create and Write to a File
file = open("sample.txt", "w")
file.write("Hello, this is a sample text file.\n")
file.write("Python file handling example.\n")
file.close()

# Read Entire File Content
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#Append Data to the File
file = open("sample.txt", "a")
file.write("This line is appended to the file.\n")
file.close()

#Read File Line by Line
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()





