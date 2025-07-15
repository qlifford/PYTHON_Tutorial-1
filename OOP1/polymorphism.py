class A:
    def show(self):
        print("from A")
class B(A): 
    def show(self):
        print("from B")
class C(A):
    def show(self):
        print("from C")
class D:
    def show(self):
        print("from D")
    ...
class E(B):
    ...
    
# obj1 = A()
obj1 = E()
obj1.show()
# print(B.mro())
# print(E.mro())