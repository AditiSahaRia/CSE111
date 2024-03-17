#Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict)

#Update value
my_dict['age'] = 27
print(my_dict)

#Add item
my_dict['address'] = 'Downtown'
print(my_dict)

squares = {1: 1, 3: 9, 4: 16, 5: 25}
print(squares)

#Removing a particular item, return value
print(squares.pop(4))
print(squares)

#Remove all items
squares.clear()
print(squares)

del squares
#print(squares) #it will show NameError as we deleted the dictionary that's why python can not recognize any variable name called square

squares = {1: 1, 3: 9, 4: 16, 5: 25}

#Removing an arbitary item, return (key,value)
print(squares.popitem())
print(squares)

#We Can not copy dictionary by this following method:
squares = {1: 1, 3: 9, 4: 16, 5: 25}
squares2 = squares #we cannot copy dictionary like this. This two variables actually refers to the same memory location
squares2[1] = 7 #this also updates the value in squares as both squares and squares2 refers to the same memory location
print(squares)

#We can copy dictionary by the following two methods :
#Using copy() function
this_dict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

my_dict = this_dict.copy()
print(my_dict)

#Using dict() function
this_dict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

my_dict = dict(this_dict)
print(my_dict)