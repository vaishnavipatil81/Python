# Simple Student Grade Management System
#list
students = []  
grades = []   

# Add student
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append(name)                   #append(): to add element at end of list
    grades.append(grade)
    print("Student added!")
    
#update Student grade
def update_grade():
    name = input("Enter student name to update: ")
    if name in students:                              
        index = students.index(name)                         
        grades[index] = float(input("Enter new grade: "))   
        print("Grade updated!")
    else:
        print("Student not found!")
        
#Remove a student from list
def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name) 
        students.pop(index)          
        grades.pop(index)             
        print("Student removed!")
    else:
        print("Student not found!")
        
 #calculate avg grade
    def average_grade():
     if grades:  
        print("Average grade:")
        print(sum(grades) / len(grades), 2)
     else:
        print("No grades available!")
        
#Calculating highest & lowest grade
    def highest_lowest():
     if grades:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))
     else:
        print("No grades available!")
        
        
 #to take a choice from user        
while True:                          
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Average Grade")
    print("5. Highest & Lowest Grades")           
    print("6. Exit")

    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        average_grade()
    elif choice == '5':
        highest_lowest()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")



    

     
        

 

