#d = {}
#dictionary -> key:value pairs
#mutable
#heterogeneous
#ordered
#we can access any values using keys

# d = {'a':10,'b':20,'c':30}
# print(d['c'])

#reassign a value in dictionary
# d = {'a':10,'b':20,'c':30}
# d['a'] = 50
# print(d)

#creating a key which does not exist.
# d['d'] = 100
# print(d)

#removing value.
#1. pop() -> remove a value present at the keys and if the key is not present returns a 
#default value
# a = d.pop('d') #pop->d -> 'd'  
# print(a)

#2. popitem() -> removes last elements or key from dictionary
# )d.popitem()
# print(d


#3. to clear a dictionary
# d.clear()
# print(d)

#4. delete
# del d
# print(d)


# dict = {'name':'bagga','age':19,'score':45.32}
# #we access all keys
# a = dict.keys()
# #we access all values
# b = dict.values()
# print(a)
# print(b)

# #for looop apki keys par lagegi
# for i in dict: #i->keys
#     print(i,dict[i])

#Iteration means= Iteration means accessing each element of a collectin ne by ne using a loop.
#dict = {'name' : 'manshi', 'age':22, 'score':98}
#for key, value in dict.items():
  #  print(key, value)



#QUESTION2.
# dict1 = {'CB':82,'DV':85, 'DM': 80}
# dict2 = {'cricket':40, 'badminton': 12, 'ludo':5}
# dict3 = {'aashi':22,'yashika':23, 'muskan':25}
# dict4 = {'aditya':23,'Rahul':24,'suraj':22}
# dict5 = {'Manshi':22,'Shalu':25,'Pragati':23}

# merged_dict = {**dict1,**dict2, **dict3,**dict4, **dict5}

# print("Merged Dictionary:",merged_dict)


#Question3.

# dict1 = {'CB':82,'DV':85, 'DM': 80}
# dict2 = {'cricket':40, 'badminton': 12, 'ludo':5}
# dict3 = {'aashi':22,'yashika':23, 'muskan':25}
# dict4 = {'aditya':23,'Rahul':24,'suraj':22}
# dict5 = {'Manshi':22,'Sh;alu':25,'Pragati':23}
# merged_dict = {**dict1,**dict2,**dict3,**dict4,**dict5}

# total = sum(merged_dict.values())
# print("merged Dictionary:", merged_dict)
# print(f"sum of value={total}")


#q.2 -> 

# d1 = {"a":10,"b":20,"c":30}
# d2 = {"d":40,"e":50}
# for i in d1:
#   if i not in d2:
#     d2[i] = d1[i]
#     print(d2)



#q.3 -> 

# d1 = {"a":10,"b":20,"c":30}
# sum = 0
# for i in d1.values():
#   sum += i

# print(sum)

#q.4 -> list to dictionary
#l = [10,20,30,40,50]
#output -> d = {0:10,1:20,2:20,3:40,4:30}
# d = {}
# for i in range(len(l)):
#   d[i] = l[i]
# print(d)




# l1 = ['a','b','c','d','e']
# l2 = [10,20,30,40,50]
# d = {}
# for i in range(len(l1)):
#   d[l1[i]] = l2[i]
# print(d)



#Q -> count the frequency of each elements

# l = [1,1,1,2,3,2,4,5,3,5,4,2,1]
# d = {}
# for i in l:
#   if i not in d:
#     d[i] = 1
#   else:
#     d[i] += 1

# print(d)


#Q -> 6. 

# d1 = {'a':10,'b':20,'c':30}
# d2 = {'d':10,'a':5,'c':10}
# for i in d2:
#   if i not in d1:
#     d1[i] = d2[i]

#   else:
#     d1[i] += d2[i]

# print(d1)


##########leetcode

# l = [3,2,3,2,2,2]
# d = {}
# for i in l:
#     if i not in d:
#       d[i] = 1
#     else:
#       d[i]+=1
# for j in d.values():
#     if j%2!=0:
#       print("false")
#       break
# print(d)

#you have give an dictionary sort the dictionary based on the values

dic = {'a':100,'b':50,'c':200}
#step 1: dictionary -> list
l = []
for i in dic:
    l.append(i,dic[i])
print(l)

  #step 2: list-> sort(bubble sort)
  # for i in range(len(l)):
  #   for j in range(i+1,len(l)):
  #     if l[i][l] > l[j][l]:
  #       l[i],l[j] = l[j],l[i]

  # print(l)





  #step 3: list->dictionary
# d = {}
# for k in l :
#    d[k[0]] = k[l]
# print(d)





































































































































































