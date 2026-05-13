#print("hello world")

#indexing

# a = "rahul"
# print(a[4])

#slicing

# a = "SHER CODER"
# print(a[0:4:1])

#data type conversion
# a = 12
# a = str(a)
# print(type(a))

##OPERATORS
#1> arithmetic operators
# a = 5
# b = 32
# print(a + b)
# print(b - a)
# print(a*b)
# print(b/a)
# print(b//a)
# print(32%5)

#2> assignment operators
# a = 20
# a = a+20
# a = a+40
# a = a+60
# print(a)

#3> comparison operators
# a = 12
# b = 12
# print(a == b)
# print(a != b)

# print(126>130)
# print((456 == 456)!=(235==236))
# print(12<10 or 45==56 or 69>70 or 15!=13)
# print(True and bool(0))

#ascii values comparison

# print(ord("A"))
# print(ord("B"))
# print("A">"B")

##CONDITIONAL STATEMENTS IF ELSE

# a = 13
# if a > 10:
#     print("i will do task A")
# else:
#     print("i will do task B")

# money = int(input("please provide me the money:-"))
# if money == 10:
#     print("i will have a choco bar icecream")
# else:
#     print("i will have a mango dolly")

#Q.1 -> Accept the two numbers and the print the greatest between them.

# num1 = int(input("please tell your first number:-"))
# num2 = int(input("please tell your second number:-"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("both the numbers are same")

#Q.2 -> Accept the gender from the user as character and print the respective greeting message

# gen = input("please tell your gender as character(M or F) ")
# if gen == 'M' or gen == 'm':
#     print("Good morning sir")
# elif gen == 'F' or gen == 'f':
#     print("Good morning mam")
# else:
#     print("unidentified gender")

#Q.3 -> Accept an integer and check whether it is an even number or odd?

# num = int(input("please tell your number:-"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# str = "rahulislazyboy"
# print(str[::-1])

# a = (2,3,10,35)
# total = sum(a)
# print(total)

# a = (2,3,10,35)
# sum = 0
# for i in a:
#     sum = sum + i
#     print(sum)

#Q.4 -> accept name and age from the user.check if the user is valid voter or not.
# name = input("tell your name:-")
# age = int(input("now tell your age:-"))
# if age >= 18:
#     print(f"hello {name} you are a valid voter")
# else:
#     print(f"hello {name} you are not a valid voter")

#Q.5-> accept a year and check if it is a leap year or not.

# year = int(input("tell your year :-"))
# if year%100 == 0 and year%400 == 0:
#     print("its a leap year")
# elif year%100 != 0 and year%4 == 0:
#     print("its a leap year")
# else:
#     print("its a normal year")

#Q.6-> if elif ladder

# t = int(input("please tell the temperature:-"))
# if t < 0:
#     print("freezing cold")
# elif t >= 0 and t < 10:
#     print("very cold")
# elif t >= 10 and t < 20:
#     print("cold")
# elif t >= 20 and t < 30:
#     print("pleasant")
# elif t >= 30 and t < 40:
#     print("hot")
# else:
#     print("temp is very hot")

#Q.7-> check even or odd

# num = int(input("tell your number:-"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

#Q.8-> pass or fail checker

# marks = int(input(" tell your marks"))
# if marks >= 40:
#     print("pass")
# else:
#     print("fail")

#Q.9-> positive,negative or zero

# num = float(input("enter a number:-"))
# if num > 0:
#     print("number is postive")
# elif num < 0:
#     print("num is negative")
# else:
#     print("num is zero")

#Q.10-> age category

# age = int(input("please enter your age:-"))
# if age < 13:
#     print("child")
# elif age >= 13 and age <=19:
#     print("teenager")
# else:
#     print("adult")

#Q.11-> temperature check
# temp = int(input("tell the temperature:-"))
# if temp >= 30:
#     print("hot day")
# else:
#     print("pleasant day")

#Q.12-> divisibility test
# num = int(input("tell the number:-"))
# if num % 3==0 and num % 5 == 0:
#     print("divisible")
# else:
#     print("not divisible")

#Q.13-> maximum of three numbers 
# a = int(input("enter first number:-"))
# b = int(input("enter second number:-"))
# c = int(input("enter third number:-"))

# if a == b or b == c or a == c:
#     print("two numbers are equal")
# else:
#     print("maximum number is",max(a,b,c))

# a = int(input("enter first number:-"))
# b = int(input("enter second number:-"))
# c = int(input("enter third number:-"))

# if a == b or b == c or a == c:
#     print("two numbers are equal")
# elif a > b and a > c:
#     print("maximum number is",a)
# elif b > a and b > c:
#     print("maximum number is",b)
# else:
#     print("maximum number is",c)

#Q.14-> login validation
# pas = input("enter password")
# if pas == "admin123":
#     print("login successful")
# else:
#     print("invalid password")

#Q.1-> Write a python program to check whether a number is even or add?

# num = int(input("please enter your number:-"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number") 

#Q.2-> if a students marks are 40 or above,print "pass",otherwise print'fail'?

# marks = int(input("enter your marks:-"))
# if marks >= 40:
#     print("pass")
# else:
#     print("fail")

#Q.3-> Take a number from the user and print whether it is positive,negative or zero?

# num = float(input("enter the number :-"))
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("number is negative")
# else:
#     print("number is zero


#Q.4-> if the temperature is 30 degree celsius or more print"hot day",else print"pleasant day"

# temp = int(input("pleasse tell the temperature:-"))
# if temp >= 30:
#     print("hot day")
# else:
#     print("pleasant day")


####### LOOPS ########

# n = int(input("which table you want ?"))
# for i in range(n,(n*10)+1,n):
#     print(i)

#Q.1-> accept an integer and hello world n times?

# n = int(input("please tell your number:-"))
# for i in range(n):
#     print("hello world")

#Q.2-> print natural numbers up to n?

# n = int(input("please tell your number:-"))
# for i in range(1,n+1,1):
#     print(i)


#Q.3-> reverse for loop print n to 1?

# n = int(input("please tell your number:-"))
# for i in range(n,0,-1):
#     print(i)

#Q.4-> Take a number as input and print its table?

# n = int(input("which table you want:-"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

#Q.5-> sum up to n terms?

# n = int(input("please tell your number:-"))
# sum= 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is {sum}")

#Q.1-> Accept an integer and print hello world n times?

# n = int(input("please tell youur number:-"))
# for i in range(n):
#     print("hello world")

#Q.2-> print natural numbers up to n?

# n = int(input("please tell your number:-"))
# for i in range(1,n+1,1):
#     print(i)


#Q.3-> Reverse for loop and print n to 1?

# n = int(input("please tell your number:-"))
# for i in range(n,0,-1):
#     print(i)


#Q.4-> Take a number as input and print its table?

# n = int(input("which table you want:-"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")


# #Q.5-> sum up to n terms?

# n = int(input("pl3ease tell your numbers:-"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is {sum}")


#Q.6-> factorial of a number?

# n = int(input("please tell your number:-"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")


#Q.7-> print the sum of all even and odd numbers in a range separately?

# n = int(input("tell your number:-"))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even},{odd}")


#Q.8-> print all the factors of a number?


# n = int(input("which number factors you want:-"))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
        

#Q.9-> Accept a number and check if it a perfect number or not.a number whose sum of factor is equal to number itself?


# n = int(input("check your number perfect or not:-"))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum = sum + i
# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")


#Q.10-> check whether the number is prime or not?

# n = int(input("check your number is prime or not:-"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")



#Q.11-> reverse a string without using inbuild function?

# a = "rahulthakur"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)


#Q.12-> check string is pallindrome or not?


# a = "NAMAN"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if b == a:
#     print("Its a pallindrome")
# else:
#     print("Ita not a pallindrome")


#Q.13-> count all letters,digits and special symbols from a given string?

# a = "sdfsogn12413@#$%^&u"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchr += 1

# print(f"your digits are {dig}\n your alphabets are {char}\n your special characters are {spchr}")



############### WHILE LOOP ###############

#Q.1-> separate each digit of a number and print it on the new line?

# a = int(input("tell your number:-"))

# while a > 0:
#     print(a % 10)
#     a = a//10


#Q.2-> Accept a number and print its reverse

# a = int(input("tell your number:-"))
 
# rev = 0

# while a > 0:
#     rev = rev*10 + a % 10
#     a = a//10
# print(rev)

#Q.3-> Accept a number and check if it is a pallindromic number(if number and its reverse are equal)

# a = int(input("tell your number:-"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev*10 + a % 10
#     a = a//10
# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")


#Q.4-> number guessing game

# import random

# num = random.randint(1,10)

# tries = 0
# while True:
#     guess = int(input("please guess your number between 1 and 10:-"))

#     if num == guess:
#         tries += 1
#         print(f"you are right you guessed the number in {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries += 1

#     elif num > guess:
#         print("go a little higher")
#         tries += 1

#     else:
#         tries += 1
#         print("sorry you are wrong")



################# FUNCTIONS ##############

# #Q.1-> check the string is pallindrome or not?

# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a pallindrome")

# pallindrome("NAMAN")
# pallindrome("CURSOR")


 

#1. create class bank
#2. CRUD operastions
#create-> create user
#read
#update
#delete




# from pathlib import Path
# import json

# class Bank:
#     database = "data.json"
#     data = [] # yeh data json me save hoga

#     try:
#         if Path(database).exists():
#             print("file exists")
#             with open(database) as fs:
#                 data = json.loads(fs.read())

#         else:
#             print("no such file exists")

#     except Exception as err:
#         print("error occured")

# obj = Bank()


#1. you have a list your task is to count the frequently occuring elements and 
#remove the most occuring

#l = [1,1,1,2,2,3,3,4,4,3,3,2,1,1,5]




#2. count pairs and leftovers from a list?
# l = [1,1,1,2,2,2,3,3,3,3]
# pairs = //2
# leftovers = %10





#3. count the number of vowels from a string?
# s = "this is the sample string"
# v = "aeiouAEIOU"
# count = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         count+=1
# print(f"no.of vowels are:{count}")



#4. check if two number are pallindrome or not?











