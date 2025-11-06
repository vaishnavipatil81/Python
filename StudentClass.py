# Program: Demonstrate a Class in Python

class Student:
    # Class attributes
    college = "ABC College"

    # Method
    def display_info(self):
        print("This is a Student class.")

# Create object of Student class
s1 = Student()
s1.display_info()

# Access class attribute
print("College Name:", Student.college)
