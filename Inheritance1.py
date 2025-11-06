# Single Inheritance

class Parent:
    def display_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def display_child(self):
        print("This is the Child class.")


obj = Child()
obj.display_parent()
obj.display_child()




# Multiple Inheritance

class Father:
    def show_father(self):
        print("This is Father class.")

class Mother:
    def show_mother(self):
        print("This is Mother class.")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class.")

obj = Child()
obj.show_father()
obj.show_mother()
obj.show_child()




#  Multilevel Inheritance

class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class.")

class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is Child class.")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()


