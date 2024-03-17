word = input()
word = word.lower()
word_list = []
for i in word:
    word_list.append(i)
i = 0
while i < len(word_list):
    count = 1
    if i < len(word_list)-1:
        for j in range(len(word_list)):
            
