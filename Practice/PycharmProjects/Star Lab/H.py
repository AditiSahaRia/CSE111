for line in range(11):
    for star in range(5):
        if star==0 or star==4 or line==5:
            print('* ', end='')
        else:
            print('  ', end='')
    print('')