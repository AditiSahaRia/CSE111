data = input()
data = data.split(', ')
keys = []
values = []

for i in data:
    keys.append(i.split(' : ')[0])
    values.append(i.split(' : ')[1])

dictionary = {}

for i in range(0, len(values)):
    values_index = []
    dict_value = []
    for j in range(0,len(values)):
        if values[j] == values[i]:
            values_index.append(j)
    for k in values_index:
        dict_value.append(keys[k])
    dictionary[values[i]] = dict_value

print(dictionary)


# In question the output is :
# { "value1" : ["key1", "key3"], "value2" : ["key2"] }
#In my code the output is:
# {'value1': ['key1', 'key3'], 'value2': ['key2']}




#key1 : value1, key2 : value2, key3 : value1
