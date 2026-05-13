# #inbuild functions


# #print("hello")

# #user-defined functions

# #def greeting(): #defining a function
#     #print("hello brother kya halchal hai")

# #greeting() # calling a function


# #parameters and arguments
#parameters -> define functions
#arguements -> call the functions

# #def addition(a,b): # parameters 
#     #print(a + b)

# #addition(20,30)#arguments
# #addition(100,300)
# #addition(34,66)
# #addition(12,45)
# #addition(85,345)


# #def count(n):
#     #if n == 21:
#         #return

#     #print(n)
#     #count( n + 1)

# #count(1)


# #def hello1():
#     #hello2()
#     #print("hello 1")

# #def hello2():
#     #hello3()
#     #print("hello2")

# #def hello3():
#     #hello4()
#     #print("hello 3")

# #def hello4():
#     #print("hello 4")
#--------------------------------------------------------------------------------------------

# def palindrome(n):
#     rev = 0
#     copy = n
#     while n > 0:
#         rev = rev * 10 + n%10
#         n = n // 10
#     if rev == copy:
#         print(f"{copy} is a palindrome")
#     else:
#         print(f"{copy} is not a palindrome")

# palindrome(121)
# palindrome(134)
# palindrome(2332)
# palindrome(765)
#-----------------------------------------------------------------------------------------

# def hello():
#     return("hello how are you")

# a = hello()
# print(a)
#----------------------------------------------------------------------------------------
# a = 17

# for i in range(2,a):
#     if a%i == 0:
#         print("not a prime number")
#         break
# else:
#     print("prime number")
#------------------------------------------------------------------------------------------

# def primechecker(a):
#     for i in range(2,a):
#         if a%i == 0:
#             return "not a prime"
#     return "prime number"

# print(primechecker(19))
# print(prdef regimechecker(56))
# print(primechecker(89))


#types of arguments/parameters

# edef hllo(a,b,c):
#     print(a + b + c)

# hello(12,c = 15,b = 13)
#you can define the parameters before
#providing the values and they are known
#as keyword arguments
#you cannot provide positional arguments
#after a keyword argument


# eteristration(paisa,name,number = "none"):
#     print(name)
#     print(paisa)
#     print(number)

# registration(50000,"rahul",8770803882)
# we can give default values to our parameters
# and we cannot create a normal parameter after 
# default parameters

# import random 
# original =  random.randint (1,100)
# tries = 0
# while True:
#     tries = tries + 1
#     if tries == 8:
#         print(f"try - {tries}")
#         break
#     guess = int(input('guess your number:-'))

#     if original == guess:
#         print("you won the game in {tries} tries")
#         break
#     eliimport f guess < original:
#         print("go a bit higher")

#     elif guess > original:
#         print("go a bit lower")


#1 - rock
#2 - paper
#3 - scissors

# random import

# comp_score = 0
# human_score = 0

# while True:
#     if human_score == 5:
#         print("you won the game congratulations")
#         break
#     if comp_score == 5:
#         print("computer won the game")
#         break
#     you = int(input("press 1 - for rock, press 2 for paper and press 3 for scissors:-"))
#     if you >3 or you < 1:
#         print("wrong input choose again")
#         continue
#     comp = random.randint(1,3)
#     if you == 1 and comp == 3:
#         human_score += 1
#         print(f"you won this round\ncurrent score -you-{human_score} and comp-{comp_score}")

#     elif you == 2 and comp == 1:
#             human_score += 1
#             print(f"you won this round\ncurrent score-you-{human_score} and comp-{comp_score}")
#     elif you == 3 and comp == 2:
#         human_score += 1
#         print(f"it was a draw\ncurrent score-you-{human_score} and comp-{comp_score}")
#     else:
#         comp_score = comp_score + 1
#         print(f"comp won this round\ncurrent score-you-{human_score} and comp-{comp_score}")









    






