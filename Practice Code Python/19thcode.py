# # today we will learn what are tupels and how to use tuples in python!! so let's start this.

# tuple=(1,21,34,32,445)
# print(type(tuple) , tuple)
# print(len(tuple))
# # print(tuple[6])
# print(tuple[3])
# # print(tuple)

# # a=int(input("Enter and check the number "))
# # if a in tuple:
# #  print ("yes , this number is in tuple")
# # else:
# #  print("this number does not exist")

# # tuple2 = tuple[1:5]
# # print(tuple2 , tuple2.count(21))

# # fruit_tuple = ('apple', 'banana', 'cherry')
# # fruit_tuple[1] = 'mango'  # This will raise a TypeError

person = ('John', 30, 'Engineer')
name, age, profession = person
print("name =" , name)      # Output: 'John'
print(age)       # Output: 30
print(profession)  # Output: 'Engineer'