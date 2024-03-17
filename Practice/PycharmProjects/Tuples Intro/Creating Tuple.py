#Empty tuple
my_tuple = ()
print(my_tuple)

#Tuple of only integer values
my_tuple = (1, 2, 4,-1)
print(my_tuple)

#Tuple of mixed data types
my_tuple = (1, 'Hello', 3.4)
print(my_tuple)
print(my_tuple[-1])
print(my_tuple[1])

#Creating One element tuple
#We have to put , after the value (in case of creating an one element tuple) otherwise python will not consider it as a tuple
my_tuple = (1,)
print(my_tuple)

#Tuple Packing
my_tuple_01 = (1, 3, 2) #int values
my_tuple_02 = (1, 'hello', -5, 3.5) #mixed values

#Tuple Unpacking
x, y, z = my_tuple_01
a, b, c, d = my_tuple_02
#u, v, w = my_tuple_02  #This will show VallueError as the tuple has four values
print(x, y, z, a, b, c, d)

#Nested Tuple
my_tuple = ('mouse', [8,4,6], (1,2,3))
print(my_tuple)
print(my_tuple[-1])
print(my_tuple[1])
print(my_tuple[0])

#Nested Tuple Indexing

print(my_tuple[0][4])
print(my_tuple[1][1])
print(my_tuple[-1][-2])

#Concatenation
print((1, 2, 3)+(4, 5, 6))

#We Can Delete the entire tuple but not a single item inside the typle
del my_tuple #this will delete the entire tuple from the memory list
#del my_tuple[1] #this is not possible as Tuples are immutable. We cannot change the tuple