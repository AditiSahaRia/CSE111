dictionary = {}
value = int(input('please enter a number: '))
dictionary[0] = value
for i in range(1,10):
    value_count = 0
    value = int(input('please enter a number: '))

    while value in dictionary.values():
        value = int(input('It is a duplicate value. Please enter another number: '))
        if value not in dictionary.values():
            dictionary[i] = value
            break

    else:
        dictionary[i] = value

print(dictionary)
