#object oriented approach
#jis class ka object hoga usi class ka attribute aur method


# class SharmaVishnu:
#     a = 10 #attribute

#     def show(self): #class method
#         print("chole bhature")
#     def display(self):
#         self.name = 'salman bhai'
#         print(f"name is {self.name}")
# mp_nagar = SharmaVishnu()
# mp_nagar.display()

# mp_nagar = SharmaVishnu()
# mp_nagar.show()
# print(mp_nagar.a)

# indrapuri = SharmaVishnu()
# indrapuri.show()
# print(indrapuri.a)


#METHODS -> classmethod,staticmethod



# class SharmaVishnu:
#     def __init__(self,waiter,table,chair):
#         self.waiter = waiter# these are instance attribute
#         self.tables = table
#         self.chairs = chair
#         print("constructor function is called")
    
#     def show(self): # instance method
#         print(f"waiter name is beautiful {self.waiter}")
#         print(f"no.of tables {self.tables}")
#         print(f"no.of chairs {self.chairs}")

# indrapuri = SharmaVishnu('salman bhai',20,10)
# indrapuri.show()


## object = instance


# you guys have to create a class as information and accept name and age from the user and just print the name
#and the age of the user



# class Info:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"the name is {self.name} and age is {self.age}")

# obj = Info("ramesh",45)
# obj.show()


# create a class bank and as class initialize it must ask the balance of user and if user call
#method deposite then it should ask money to be deposite and add it to balance then display updated balance


# class Bank:
#     def __init__(self,balance):
#         self.balance = balance
#         print(f"The balance is {self.balance}")

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"The updated amount is {self.balance}")

# obj2 = Bank(5000)
# obj2.deposit(2000)


# class student:
#     college = "SIRT" #class attribute

#     @classmethod
#     def change_college(self,new_name):
#         cls.college = new_name


# class SharmaVishnu:
#     def __init__(self,waiter):
#         self.waiter = waiter

#     def show(self):
#         print(f"name of the waiter is {self.waiter}")

# obj1 = SharmaVishnu("nathulal")
# obj1.show()


# class SharmaVishnu:
#     def __init__(self,waiter):
#         self.waiter = waiter


#     @staticmethod #these are independent of object
#     #object bnao ya na bnao same.async

#     def show(waiter):
#         print("name is:",waiter)

# obj = SharmaVishnu("nathulal")
# SharmaVishnu.show("ramu")


# class SharmaVishnu:
#     def __init__(self,dish,price):
#         self.dish = dish
#         self.price = price
#         self.__revenue = 30000 #private instance attribute
#     @property # getter
#     def show(self):
#         print(f"dish is {self.dish}")
#         print(f"price is {self.price}")
#         print(f"revenue is {self.__revenue}")

#     @show.setter # setter
#     def change_dish(self,new):
#         self.__revenue = new

# Paaji = SharmaVishnu("paneer kulche,3+ kulche",180)
# Paaji.change_dish = 40000 #(4000)
# Paaji.show #()


#agar private attribute ko method se change kar rahe ho to setter hota hai
#agar private attribute ko method se call kar rahe ho to getter hota hai



#1. Class Bank -> name,age,address,amount -> += __balance

# class Bank:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__balance = 500000

#     @property
#     def show(self):
#         print(f"name is {self.name},age is {self.age},address is {self.address} and balance is {self.__balance}")
    
#     @show.setter
#     def change_balance(self,amount):
#         self.__balance += amount


# user1 = Bank("virat",52,"nahi pata")
# user1.change_balance = 500000
# user1.show


# class Animal:
#     def __init__(self,name,age):
#         self.name = name #instance attribute
#         self.age = age
#         self.can_walk = True
#         self.__gender = "male"

#     def show(self):
#         print(f"name is {self.name} and  age is {self.age}")

#     def sleep(self):
#         self.can_walk = False


#     def gender(self):
#         print(f"gender of my animal is {self.__gender}")


# class Cat(Animal):
#     def __init__(self,name,age,breed):
#         super().__init__(name,age)
#         self.breed = breed


#     def show2(self):
#         print(f"this is cat class {self.name},{self.age},{self.breed}")


# obj = Cat("Tom",4,"Persian")
# obj.
# obj.show()











































        







