collumn = 11
row = 5

for line in range(4):
    for star in range(5):
        if star==0 or (star==4 and line!=0) or (line==0 and star!=4):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()

for line in range(3):
    for star in range(5):
        if star==0 or (star==4 and line!=0) or (star==3-line):
            print('*  ', end='')
        else:
            print('   ', end='')

    print()

for line in range(4):
    for star in range(5):
        if star==0 or (star==4 and line!=3) or (line==3 and star!=4):
            print('*  ', end='')
        else:
            print('   ', end='')

    print()
