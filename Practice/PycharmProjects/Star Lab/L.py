collumn = 11
row = 5

for line in range(collumn):
    for star in range(row):
        if line==collumn-1 or star==0 or(star==row-1 and line==collumn-2):
            print('* ', end='')
        else:
            print('  ', end='')
    print('')