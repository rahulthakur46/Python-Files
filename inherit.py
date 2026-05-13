#1-> multiple inheritance.

# class Bank:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"this is bank class {self.name}")

# class Account:
#     def __init__(self,account_no):
#         self.account_no = account_no

#     def show2(self):
#         print(f"this is account class {self.account_no}")

# class Customer(Bank,Account):
#     def __init__(self,name,account_no):
#         Bank.__init__(self,name)
#         Account.__init__(self,account_no)
#     def show3(self):
#         print(f"this is customer class")

# obj = Customer("vijay","65456487894")
# obj.show()
# obj.show2()
# obj.show3()
# #jab 2 ya 2 se jyada type ke inheritance mix ho jaaye -> hybrid inheritance



# class Papa:
#     def skill(self):
#         print("belt hi belt")
# class Mother:
#     def skill(self):
#         print("de taane")

# class Child(Papa,Mother): #multiple inheritance
#     def skill(self):
#         print("na padhna or na padhne dena")

# class Student(Child):  #multilevel inheritance
#     def skill(self):
#         print("chit bana de")


# #ek parent multiple childs -> hierarchical inheritance

# class A:
#     def show(self):
#         print("this is A class")
# class B(A):
#     pass
# class C(A):
#     pass



## poly Morphism - 2 types -> compile time . run time 
# compile time - method overloading and run time - method overriding

# method overloading(compile runtime- ye lang.python me nahi hoti hai)

# class Sample:
#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)

# obj = Sample()
# obj.add(10,20)


# method overriding(duck_typing)

# class Parent:
#     def skill(self):
#         print("this is parent class")
#     def show(self):
#         print("zero civic sense")

# class Child(Parent): #single level inheritance
#     def skill(self):
#         print("this is Child class")

#     def show(self):
#         print("balle balle")


# obj2 = Parent()
# obj2.skill()
# obj = Child()
# obj.skill()
# obj.show()

# Create a class named as bank and accept the amount,name,pin,address from bank holder and
#hide the balance of the holder at last update the balance and show the updated amount to user


class Bank:
    def __init__(self,name,pin,account,address):
        self.__balance = 10,000 # private
        self.name = name
        self.pin = pin
        self.account = account
        self.address = address

    def update(self,amount):
        self.__balance += amount
        print(f"{self.name},{self.pin},{self.__balance},{self.account}")

class Money(Bank):
    def __init__()
















