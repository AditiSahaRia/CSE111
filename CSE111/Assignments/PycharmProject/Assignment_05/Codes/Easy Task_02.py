string = input()
string_list = string.split(',')
dictionary = {}
new_dictionary = {}

value_dict = []
key_dict = []

for i in string_list:
    new_list = i.split(':')
    new_list[0]=new_list[0].replace(' ','')
    key_dict.append(new_list[0])
    new_list[1] = new_list[1].replace(' ', '')
    dictionary[new_list[0]] = int(new_list[1])
    value_dict.append(int(new_list[1]))

max_value = value_dict[0]
min_value = value_dict[0]

min_index = 0
max_index = 0

for i in range(len(value_dict)):
    if value_dict[i] > max_value:
        max_value = value_dict[i]
        max_index = i
    elif value_dict[i] < min_value:
        min_value = value_dict[i]
        min_index = i

print(f'Minimum: {key_dict[min_index]}')
print(f'Maximum: {key_dict[max_index]}')

