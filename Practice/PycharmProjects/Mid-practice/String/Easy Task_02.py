word = input()
new_word = ''
first_list = []
second_list = []
for i in word:
    first_list.append(i)

for i in first_list:
    if i == ' ':
        second_list.append(ord(i))
    else:
        second_list.append(ord(i)+1)

for i in second_list:
    new_word += chr(i)

print(new_word)