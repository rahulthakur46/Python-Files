#Tuples
#1> ordered->indexing
#2> allows duplicacy
#3> immutable

# t = ()
# print(type(t))


# t = (10,20,30)
# print(t[0])

#assigning
# t = (10,20,30)
# t[1] = 50
# print(t)

#1 .count() -> count how many times a number occured
#2 .index() -> index value of a numner or elements

# t1 = (1,1,1,2,2,3,3,1,4,2)
# print(t1.count(1))
# print(t1.index(1))


# two imp functions
#*args -> works on tuples
# def add(a,b,*chacha):
#     print(type(chacha))
#     print(sum(chacha))
# add(1,2,3,4,5,6,7,8,9,0)

#**kwargs -> dictionary ke form
#keyword arguments

# def info(**Rahu):
#     for key,value in Rahu.items():
#         print(key,value)
# info(name = "Rahul",age = 21,gender = "nd")



