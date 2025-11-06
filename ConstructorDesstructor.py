#  Constructor 

class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called! Object created.")

    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Vaishnavi", 21)
s1.display()



#  Destructor



class Student:
  
    def __init__(self, name):
        self.name = name
        print("Object created for", self.name)

    def __del__(self):
        print("Destructor called! Object destroyed for", self.name)

s1 = Student("Vaishnavi")

del s1





