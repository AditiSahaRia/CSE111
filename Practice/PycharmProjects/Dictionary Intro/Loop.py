#Print all the values in dictionary
#Short and Simple way
squares = {1: 1, 3: 9, 5: 25,  9: 81, 7: 49}
for i in squares:
    print(squares[i], end=', ')
print('')

#smarter way
for i in squares:
    if i == list(dict.keys(squares))[-1]:
        print(squares[i], end='.\n')
    else:
        print(squares[i], end=', ')
#Printing the output in a sorted way
squares_list = sorted(dict.keys(squares))   #Firstly creating a sorted list of keys of the dictionaries
print(squares_list)   #Checking if the list is correct or not
for i in squares_list:
    if i == squares_list[-1]:
        print(squares[i], end='.\n')
    else:
        print(squares[i], end=', ')

#Making a list of the dictionary
squares_list = list(squares.items())
print(squares_list)

#Printing all the values and keys if dictionary
#Short and simple way
for x, y in squares.items():
    print(x, ':', y, end=' ')
    #print(f'{x} : ', end=', ')
print('')

#Smarter Way
for x, y in squares.items():
    if x == list(dict.keys(squares))[-1]:
        print(f'{x} : {y}', end='.\n')
    else:
        print(f'{x} : {y}', end=', ')

#assigning value with for loop
squares = {}
for i in range(6):
    squares[i] = i*i

print(squares)

#Assigning values with if condition
#Traditional Way
odd_squares = {}
for i in range(11):
    if i%2 != 0:
        odd_squares[i] = i*i
print(odd_squares)

#Smarter and simpler way
odd_squares = {i: i*i for i in range(11) if i%2 != 0}  #Here i: i*i means i=i*i
print(odd_squares)

