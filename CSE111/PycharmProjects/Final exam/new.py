string = input()
scnd_string = input()
string = string.split(',')
integer_list = []
for i in string:
    i = int(i)
    integer_list.append(i)

dictionary = {}
product = 1
for k in range(0, len(integer_list)):
    product = product*integer_list[k]
    dictionary[k] = product

frst = scnd_string.split(' ')[0]
frst = int(frst)-1
scnd = scnd_string.split(' ')[1]
scnd = int(scnd)


print(dictionary)
print(dictionary[scnd]/dictionary[frst])
