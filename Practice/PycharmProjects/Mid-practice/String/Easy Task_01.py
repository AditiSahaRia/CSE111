word = input()
sorted_word = ''
word_list = []

for i in word:
    word_list.append(i)

for i in range(len(word_list)):
    min = i
    for j in range(i+1,len(word_list)):
        if word_list[j] < word_list[min]:
            min = j
    temp = word_list[i]
    word_list[i] = word_list[min]
    word_list[min] = temp

for i in word_list:
    sorted_word += i

print(sorted_word)