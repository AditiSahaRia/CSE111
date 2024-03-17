for line in range(11):
    for star in range(5):
        if line==0 or star==2:
            print('* ', end='')
        else:
            print('  ', end='')
    print('')