# sets
#1. unordered, no indexing
#2. {} -> comma separated
#3. unique elements store
# s = {}

# l = [1,1,1,2,3,2,4,5,3,5,4,2,1]
# s = set(l)#built in function
# print(s)

# #1. .add()
# s.add(6)
# print(s)

# #2. .pop()
# s.pop()# -> first element delete
# print(s)

# #3. .remove() #we need to give elements
# s.remove(4)
# print(s)


#1> Intersection
# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6}
# print("Intersection->",s1.union(s2))

# #2> Union
# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6}
# print("Union->",s1.union(s2))

# #3> Difference(s1 - s2) -> s1 mai hai but s2 me nahi
# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6}
# print("Difference->",s1.Difference(s2))
# print("Difference->",s2.Difference(s1))

# #4> symmetric_Differnce -> jo common nahi hai
# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6}
# print("symmetric_differnce",s1.symmetric_differnce(s2))


num = 2932
a = list(str(num))
a.sort()
n1 = int(a[0]*10 + int(a[-1]))
n2 = int(a[1]*10 + int(a[-2]))

