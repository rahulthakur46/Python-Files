# # #year = int(input("tell your year :-"))

# # #if year % 100 == 0 and year % 400 == 0:
# #     #print("your year is leap year")

# # #elif year % 100 != 0 and year % 4 == 0:
# #     #print("leap year")

# # #range (start,stop,steps)
# # #you can use loops for multiple purpose
# # # for i in range(1,101,1):
# #     #print("hello world")


# # #for i in range(200,351,1):
# #     #print(i)
# # #for i in range(-1,-51,-1):
# #     #print(i)
# # #for i in range(50,-51,-1):
# #     #print(i)
# # #a=int(input("what table you want :-"))

# # #for i in range(a,(a*10)+1,a):
# #     #print(i)


# # a=int(input("Enter your number"))
# # if a>10:
# #     print("your number is greater than 10")

# # else:
# #     print("not greater than 10")    

# val=int(input("Enter a number:-"))
# print("value is greater than 10"if val>10 else "value is less than or equal to 10")


#TERNARY if-else= agar if ki condition true hai to if ke left bali condition run karegi else right bali condition chalegi

#num=int(input("enter a number:"))
#if num % 2 == 0:
    #print("even number")
#else:
    #print("odd number")


#val = int(input("enter your number:"))
#a = "positive number" if val>0 else "neg number" if val <0 else "zero"
#print(a)


#a= int(input("which number factorial you want :-"))
#fact = 1
#for i in range( 1,a+1):
    #fact = fact * i
#print(fact)


#n=int(input("tell your range:-"))

#for i in range(1,n+1):
    #if i%3 == 0 or i%5 == 0:
        #print(i)


#n = int(input("tell your number:-"))

#for i in range(1,n+1):
    #if n%i == 0:
        #print(i)


#n = int(input("tell your number:-"))
#sum = 0
#for i in range(1,n+1):
    #if n%i == 0:
        #sum = sum + i

#print(sum)

#prime numbers

#if factors more than 2 = not a prime number

#n = int(input("enter a number"))
#factors = 0
#for i in range(1,n+1):
    #if n % i == 0:
        #factors +=1
#if factors > 2:
    #print("not prime number")
#else:
    #print("prime number")

#n= int(input("enter a number"))
#factors = 0
#for i in range(2,n):
    #if n % i == 0:
        #print("not prime")
        #break
    #else:
        #print("prime")
        #break

#n = 1234
#while n > 0:
    #last = n % 10
    #print(last)
    #n = n // 10

    # % use karte hai to extract last digit and print it
    # // use karte hai to remove last digit



#loops
#for loop - range
#while loop - condition

#while loops


#i = 1
#while i <= 5: - initialization
    #print("hello world") - code ka block
    #i = i+1 - increment

#i = 1
#while i <=10:
    #print(i)
    #i+=1

#i = 10
#while i >=1:
    #print(i)
    #i -=1


#while True:
    #n = int(input('enter your number:'))
    #print(n)
    #if n == 0:
        #print("while loop break")
        #break


#you have to take input until you found a number which is divisible by both 3 and 5


#while True:
    #n= int(input("enter your number:"))
    #print(n)
    #if n%3 and n%5:
        #print(divisible)


#1. take input until.
#2. until input is divisible by 3 and 5

#while True:
    #n = int(input("enter number"))
    #if n % 3 == 0 and n % 5 == 0:
        #print(f"The number {n} is divisible by both 3 and 5")
        #break

#hcf question
#n1 = int(input("enter first number:"))
#n2 = int(input("enter second number:"))

#smaller = 0
#if n1 < n2:
    #smaller = n1
#else:
    #smaller = n2

#hcf = 1 - global variables
#for i in range(1,smaller+1):
    #if n1 % i == 0 and n2 % i == 0:
        #hcf = i-l0cal variables
#print(hcf)


#n1=int(input("enter first number:"))
#n2=int(input("enter second number:"))
#smaller = 0
#if n1 <n2:
    #smaller =n1
#else:
    #smaller = n2

#hcf = 1
#for i in range(smaller,0,-1):
    #if n1%i == 0 and n2 %i == 0:
        #hcf = i
        #break
#print(hcf)


#n=5
#for i in range(1,n+1):
    #print(i*'*')


#for loops backup class

#1. for loops runs till a range
#2. while runs until a condition become false

#for loop -> range(_,_,_)
#1. start -> default = 0
#2. stop -> n - 1
#3. step -> default = 1

#for i in range(1,10,1):
    #print(i)

#in is the member operator

#name = "shaurya"
#for i in name:
    #print(i)

#name = "shaurya"
#for i in range(len(name)):
    #print(name[i])


#sum from 1 - 10

#sum = 0
#for i in range(1,11):

    #sum = sum+i

    #print(sum)


#str="hello how are you"
#count=0
#for i in str:
    #if i in "aeiouAEIOU":
        #count+=1

#print(f"total number of vowels are {count}")


#a = 0
#b = 1
#n = int(input("enter series:"))
#for i in range(n):
    #print(a)
    #a,b = b, a+b

#armstrong number

#n = 145
#while n > 0:
    #digits = n % 10 # last digits extracts
    #print(digits)
    #n = n // 10 # remove digits

#n = 145
#copy = n
#sum = 0
#while  n > 0:
    #digits = n % 10
    #sum = sum + digits ** 3
    #n = n // 10
#if sum == copy:
    #print("armstrong")
#else:
    #print("not an armstrong")























    









    



