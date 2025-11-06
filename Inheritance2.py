#  Hierarchical Inheritance

class Parent:
    def show_parent(self):
        print("This is Parent class.")

class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class.")

class Child2(Parent):
    def show_child2(self):
        print("This is Child2 class.")

obj1 = Child1()
obj2 = Child2()

obj1.show_parent()
obj1.show_child1()

obj2.show_parent()
obj2.show_child2()


#  Hybrid Inheritance

class A:
    def show_A(self):
        print("This is Class A.")

class B(A):
    def show_B(self):
        print("This is Class B.")

class C(A):
    def show_C(self):
        print("This is Class C.")

class D(B, C):
    def show_D(self):
        print("This is Class D.")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()
