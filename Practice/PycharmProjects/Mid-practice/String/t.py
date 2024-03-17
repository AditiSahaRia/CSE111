dictionary = {}
word = input()
word= word.lower()
word_list = []
for number in word:
    if number in dictionary:
        dictionary[number] = dictionary.get(number)+1
    else:
        dictionary[number] = 1

for i in dictionary:
    print(f'{i} - {dictionary.get(i)}', end=' ')