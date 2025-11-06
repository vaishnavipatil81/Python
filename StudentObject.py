# Program: Demonstrate Object in Python

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

# Create objects of the class
student1 = Student("Vaishnavi", 101)
student2 = Student("Aarav", 102)

# Access data using objects
student1.display()
student2.display()
