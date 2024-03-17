a = input()
b = a.split('"')
a = b[1]
dict = {}
for i in a:
    b= a.count(i)
    dict[i] = b

for i in dict:
    if dict[i]!=1:
        print(f'{dict[i]}{i}', end='')
    else:
        print(f'{i}', end='')

print()