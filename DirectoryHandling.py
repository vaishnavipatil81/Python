#Import OS Module
import os


#Get Current Working Directory
print(os.getcwd())

#. Create a New Directory
os.mkdir("NewFolder")


#List All Files and Folders
print(os.listdir())

#Rename the Directory
os.rename("NewFolder", "RenamedFolder")

#Remove the Directory
os.rmdir("RenamedFolder")
