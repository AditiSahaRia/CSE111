word = input()
word_list = []
for i in word:
    word_list.append(i)

for i in range(len(word_list)):
    min = i
    for j in range(i+1, len(word_list)):
        if word_list[j]<word_list[min]:
            min = j

    temp = word_list[i]
    word_list[i] = word_list[min]
    word_list[min] = temp


new_word = ''
for i in word_list:
    new_word += i

i = 0
while i < len(word_list):
    count = 1
    if i < len(word_list)-1:
        for j in range(i+1,len(word_list)):
            if word_list[j] == word_list[i]:
                count += 1
            else:
                break
    if count > 1:
        print(f'{word_list[i]} has been counted {count} times in the word {word}')
        print('Please enter another number')
        break
    i += count
else:
    print(f'You entered {word}')