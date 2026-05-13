#how to create a list

# s = int(input("how many elements you want :-"))
# l = []

# for i in range(s):
#     z = int(input("tell your elements :-"))
#     l.append(z)

# print(l)

# a = [10,20,30,40,50]

# for i in a:    #only accessing values
#     print(i)

# for i in range(len(a)):  #accssing both index and values a[i]
#     print(a[i])

# print the sum of all the elements?
# a = [10,20,30,40,50]
# sum = 0
# for i in a:

#     sum = sum + i
#     print(sum)

# print odd and even number?
# a = [1,2,3,4,5]
# odd = 0
# even = 0
# for i in a:
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even sum is {even} and odd sum is {odd}")

# reverse ?
# a = [10,20,30,40,50]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# l = [2,96,69,77,145,20]
# max = l[0]
# index = 0
# for i in range(1,len(l)):
#     if max<l[i]:
#         max = l[i]
#         index = i

# print(f"the maximum number is {max} and it's index is {index}")
 
#find the smallest number and its index too

# l = [2,96,69,77,145,20]
# min = l[0]
# index = 0
# for i in range(1,len(l)):
#     if min > l[i]:
#         min = l[i]
#         index = i
# print(f"the minimum number is {min} and its index {index}")

# l = [2,96,69,77,145,20]
# #mean = sum of total/ no.of items (len(l))
# sum = 0
# for i in l:
#     sum = sum + i

# print(f"average of list is {sum/len(l)}")

# l = [1,2,1,1,3,3,4,1,2,3,4]
# #new l = [1,2,3,4]
# new_l = []
# for i in l:
#     if i not in new_l:
#         new_l.append(i)
# print(new_l)



#l = [2,3,15,15,3,2]
#pallindrome -> aaage se padho ya peeche se padho same hota hai
#1. to reverse our original list
#2. if the original list amd reverse list are same then it is pallindrome

# rev_l = []
# for i in range(len(l)-1,-1,-1):
#     rev_l.append(l[i])
# print(rev_l)

# l = [2,3,15,15,3,2]
# rev_l = []
# for i in range(len(l)-1,-1,-1):
# if l == rev_l:
#     print("pallindrome")
# else:
#     print("not pallimdrome")



#sorting 


#bubble sort
# l = [10,2,9,6,7,4,3,8,1]
# for j in range(len(l)): # to sort all the elements fot list
#     for i in range(len(l)-1): # i-> 0,1,2,3,4,5,6,7,8,9
#         if l[i] > l[i+1]:
#             l[i] , l[i+1] = l[i+1] , l[i]
# print(l)



#selection sort
#---------------------------------------------------------------------------------------------

#list backup class, date- 10 january 2026
# lst_2 =[12,23,34,45,567,23]
# even = 0
# odd = 0
# for i in lst_2:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even,odd)
















