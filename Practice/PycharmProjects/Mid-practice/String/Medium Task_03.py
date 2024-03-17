first_word = input()
second_word = input()

word_list = []
second_list = []

for i in first_word:
    word_list.append(i)

word_list.append(' ')

for i in second_word:
    word_list.append(i)

new_word = ''

for i in word_list:
    new_word += i

sum = 0

for i in word_list:
    if i != ' ':
        sum += ord(i)

print(new_word)
print(sum)