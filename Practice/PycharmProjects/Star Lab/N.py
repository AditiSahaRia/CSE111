collumn = 11
row = 5

for line in range(collumn):
    for star in range(2*row+1):
        if star==0 or star==2*row or star==line:
            print('* ', end='')
        else:
            print('  ', end='')
    print()