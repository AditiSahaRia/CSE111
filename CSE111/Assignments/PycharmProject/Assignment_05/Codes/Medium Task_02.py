dictionary = {}

while True:
    number = input()
    if number == 'STOP':
        break
    else:
        number = int(number)
        if number in dictionary:
            dictionary[number] = dictionary.get(number)+1
        else:
            dictionary[number] = 1

for i in dictionary:
    print(f'{i} - {dictionary.get(i)} times')