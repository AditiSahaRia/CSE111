string = input()
string_list = string.split(',')
print(string_list)
dictionary = {}
new_dictionary = {}
for i in string_list:
    new_list = i.split(':')
    new_list[0]=new_list[0].replace(' ','')
    new_list[1] = new_list[1].replace(' ', '')
    dictionary[new_list[0]] = int(new_list[1])
    print(new_list[1])
print(dictionary)

value_list = dictionary.values()
print(value_list)

number = input()
while number != 'STOP':
    number = int(number)
    ans = number in dictionary.values()
    print(ans)
    #another way
    #print(number in value_list)
    number = input()

#a: 100, b: 200, c: 300, d: 400
