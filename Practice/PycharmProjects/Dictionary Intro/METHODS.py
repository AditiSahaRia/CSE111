#In Python# comp(dict1,dict) does not work.
#If we try to use this method in python3 than it will show INVALID SYNTAX

squares = {1: 1, 3: 9, 4: 16, 5: 25}
print(squares.items())
print(squares.keys())

marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)

for i in marks.items():
    print(i)

print(list(sorted(marks.keys())))

print(all(squares))
#all() function will check if all the keys in the dictionary is greater than 0 or not.
# if key value is greater than 0 than it returns True else it returns False.
#all() function actually works for checking if the dectionary has any key value = 0


print(any(squares))
#any() functions checks if a dictionary has at least one key value which is greater than 0
#if none of the key values are greater than 0 than it will return False else it will return true


print(len(squares))

print(sorted(squares))

ict = {'Name': 'Harry', 'Roll_no': 30, 'Dept': 'CSE', 'Marks': 97}

#Printing the key values of the dictionary
print(dict.keys(ict))
#or
print(ict.keys())

#Printing the values assigned in the keys of the dictionary
print(ict.values())
#or
print(dict.values(ict))