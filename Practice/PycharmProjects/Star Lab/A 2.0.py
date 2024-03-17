line_number = 6
print(' '*6,end='')
print('*')
for line in range(6):
    space_number = line_number-line-1
    for space in range(space_number):
        print(' ',end='')

    for star in range(line+1):
        if star==0 or line==2:
            print('*',end='')
        else:
            print(' ', end='')

    for star in range(line+1):
        if star==0 or star==2*line:
            print('*', end='')

    print('')
