frst = input()
scnd = input()
dictionary = {}
for i in range(0, len(frst)):
    dictionary[i] = frst[i]

#print(dictionary)

for i in scnd:
    if i not in dictionary.values():
        print('Those strings are not anagrams.')
        break

else:
    print('Those strings are anagrams.')