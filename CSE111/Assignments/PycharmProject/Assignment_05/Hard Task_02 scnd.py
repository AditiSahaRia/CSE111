sentence = input()
sentence = sentence.upper()
dictionary = {'.,?!:': 1, 'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9, ' ': 0}

for i in sentence:
    for j in dictionary.keys():
        if i in j:
            
            break