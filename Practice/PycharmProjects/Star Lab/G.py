for line in range(11):
    for star in range(5):
        if line==0 or line==10 or star==0 or (star==4 and line>5) or (line==5 and star>1) or (star==2 and line==6):
            print('*  ', end='')
        else:
            print('   ', end='')
    print('')