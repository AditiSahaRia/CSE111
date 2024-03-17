word = input()
for i in word:
    count = 0
    for j in word:
        if j==i:
            count += 1
    print(f'{i} = {count}', end=' ')