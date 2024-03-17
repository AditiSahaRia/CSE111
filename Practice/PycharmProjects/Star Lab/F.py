for line in range(11):
    for star in range(5):
        if star==0 or line==0 or (line==5 and star<4):
            print('* ', end='')
        else:
            print('  ', end='')
    print()