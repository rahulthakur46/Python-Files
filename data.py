#ABC (Abstract base class)
#abstractmethod

#data abstraction python mai directly use nahi hota

# from abc import ABC,abstractmethod

# class SharmaVishnu(ABC):
#     def greet(self):
#         print("welcome to sharma vishnu class")

#     @abstractmethod
#     def menu(self):
#         pass

#     @abstractmethod
#     def details(self):
#         pass

# class Minal(SharmaVishnu):

#     def show(self):
#         print("this is minal class")

#     def menu(self):
#         print("paneer kulche, paneer cheese sandwich")

#     def details(self):
#         print("details...")


# obj = Minal()
# obj.details()
# obj.greet()
# obj.menu()
# obj.show()


# from abc import ABC,abstractmethod

# class BankApp(ABC):
#     def database(self):
#         print("database create and accessed")

#     @abstractmethod
#     def account(self): #abstract method
#         pass

# class WebApp(BankApp):
#     def acount(self): #concrete method
#         print("account accessed")

# class MobApp(BankApp):
#     def account(self):
#         print("this is account of MobApp class")


# obj = WebApp()
# obj.database()
# obj.account()

# obj2 = MobApp()
# obj2.database()
# obj.account()




