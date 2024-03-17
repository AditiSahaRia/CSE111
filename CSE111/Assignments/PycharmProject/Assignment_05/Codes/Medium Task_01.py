first_string = input()
second_string = input()

first_list = first_string.split(',')
first_dictionary = {}
first_key_list = []
first_value_list = []

for i in first_list:
    new_list = i.split(':')
    new_list[0]=new_list[0].replace(' ','')
    first_key_list.append(new_list[0])
    new_list[1] = new_list[1].replace(' ', '')
    first_value_list.append(int(new_list[1]))
    first_dictionary[new_list[0]] = int(new_list[1])

second_list = second_string.split(',')
second_dictionary = {}
second_key_list = []
second_value_list = []

for i in second_list:
    new_list = i.split(':')
    new_list[0] = new_list[0].replace(' ', '')
    second_key_list.append(new_list[0])
    new_list[1] = new_list[1].replace(' ', '')
    second_value_list.append(int(new_list[1]))
    second_dictionary[new_list[0]] = int(new_list[1])

new_dictionary = {}
value_sum_list = ()

for i in range(len(first_key_list)):
    for j in range(len(second_key_list)):
        if second_key_list[j] == first_key_list[i]:
            first_dictionary[first_key_list[i]]=first_value_list[i]+second_value_list[j]
            break
        elif first_key_list[i] not in second_key_list:
            pass
        if second_key_list[j] not in first_key_list:
            first_dictionary[second_key_list[j]] = second_value_list[j]
value_sum_list = []
for i in first_dictionary:
    value_sum_list.append(first_dictionary.get(i))

for i in range(len(value_sum_list)):
    min = i
    for j in range(i+1,len(value_sum_list)):
        if value_sum_list[j] < value_sum_list[min]:
            min = j
    temp = value_sum_list[i]
    value_sum_list[i] = value_sum_list[min]
    value_sum_list[min] = temp

value_sum_tupple = ()

for i in value_sum_list:
    if i in value_sum_tupple:
        pass
    else:
        value_sum_tupple += (i,)

print(first_dictionary)
print(value_sum_tupple)


#a: 100, b: 100, c: 200, d: 300
#a: 300, b: 200, d: 400, e: 200