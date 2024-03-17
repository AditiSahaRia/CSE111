collumn = 11
row = 6
first_part = collumn//2
second_part = collumn-first_part

for line in range(first_part):
    for star in range(row):
        if star==0 or star==first_part-line:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print('*')
for line in range(second_part-1):
    for star in range(row):
        if star==0 or star==line+1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()