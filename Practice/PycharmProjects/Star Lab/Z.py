collumn = 10
row = 6

print('* '*row)

for line in range(collumn):
    space_number = collumn - line - 1
    for space in range(space_number):
        print(' ', end='')

    for star in range(row):
        if star == 0 or line==collumn-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()