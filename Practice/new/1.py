def name(letter):
    if letter=='A':
        line_number = 6
        print(' ' * 6, end='')
        print('*')
        for line in range(6):
            space_number = line_number - line - 1
            for space in range(space_number):
                print(' ', end='')

            for star in range(line + 1):
                if star == 0 or line == 2:
                    print('*', end='')
                else:
                    print(' ', end='')

            for star in range(line + 1):
                if star == 0 or star == 2 * line:
                    print('*', end='')
            print('')
        print()

    elif letter=='B':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if star == 0 or (star == 4 and line != 0) or (line == 0 and star != 4):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(3):
            for star in range(5):
                if star == 0 or (star == 4 and line != 0) or (star == 3 - line):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()

        for line in range(4):
            for star in range(5):
                if star == 0 or (star == 4 and line != 3) or (line == 3 and star != 4):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()

    elif letter=='C':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if (star == 0 and line != 0) or (star == 4 and line == 1) or (line == 0 and (star != 0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if (star == 0 and line != 3) or (star == 4 and line == 2) or (line == 3 and (star != 0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='D':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if star == 0 or (star == 4 and line != 0) or (line == 0 and star != 4):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if star == 0 or (star == 4 and line != 3) or (line == 3 and star != 4):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='E':
        for line in range(11):
            for star in range(5):
                if (star == 0 and (line != 0 or line != 10)) or (line == 0 and star != 0) or (
                        line == 10 and star != 0) or (line == 5 and star < 4):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='F':
        for line in range(11):
            for star in range(5):
                if star == 0 or line == 0 or (line == 5 and star < 4):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='G':
        for line in range(11):
            for star in range(5):
                if line == 0 or line == 10 or star == 0 or (star == 4 and line > 5) or (line == 5 and star > 1) or (
                        star == 2 and line == 6):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print('')
        print()
    elif letter=='H':
        for line in range(11):
            for star in range(5):
                if star == 0 or star == 4 or line == 5:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
        print()
    elif letter=='I':
        for line in range(11):
            for star in range(5):
                if line == 0 or line == 10 or star == 2:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
        print()
    elif letter=='J':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if (star == 0 and line == 0) or (star == 4 and line != 0) or (line == 0 and (star != 0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if (star == 4 and line != 3) or (line == 3 and (star != 0 and star != 4)):
                    print('*  ', end='')
                elif (star == 0 and (line==1 or line == 2)) :
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='K':
        collumn = 11
        row = 6
        first_part = collumn // 2
        second_part = collumn - first_part

        for line in range(first_part):
            for star in range(row):
                if star == 0 or star == first_part - line:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print('*')
        for line in range(second_part - 1):
            for star in range(row):
                if star == 0 or star == line + 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='L':
        collumn = 11
        row = 5

        for line in range(collumn):
            for star in range(row):
                if line == collumn - 1 or star == 0 or (star == row - 1 and line == collumn - 2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
        print()
    elif letter=='M':
        collumn = 11
        row = 5

        for line in range(collumn):
            for star in range(2 * row + 1):
                if star == 0 or star == 2 * row or (line < collumn // 2 + 1 and star == line) or (
                        line < collumn // 2 and star == 2 * row - line):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='N':
        collumn = 11
        row = 5

        for line in range(collumn):
            for star in range(2 * row + 1):
                if star == 0 or star == 2 * row or star == line:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='O':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if (star == 0 and line!=0) or (star == 4 and line!=0) or (line == 0 and (star!=0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if (star == 0 and line!=3) or (star == 4 and line != 3) or (line == 3 and (star!=0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='P':
        collumn = 11
        row = 5

        for line in range(5):
            for star in range(5):
                if (star == 0 and line!=0) or (line == 0 and (star!=0 and star != 4)):
                    print('*  ', end='')
                elif (star == 4 and (line!=0 and line!=4)) or (line==4 and star!=4):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(3):
            for star in range(5):
                if star == 0: #(star == 0 and line!=3) or (star == 4 and line != 3) or (line == 3 and (star!=0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='Q':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if (star == 0 and line != 0) or (star == 4 and line != 0) or (line == 0 and (star != 0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if (star == 0 and line != 3) or (star == 4 and line != 3) or (line == 3 and (star != 0 and star != 4)):
                    print('*  ', end='')
                elif star==2 and line==2:
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print((' '*12)+"*")
        print()
    elif letter=='R':
        collumn = 11
        row = 5
        for line in range(5):
            for star in range(5):
                if (star == 0 and line!=0) or (line == 0 and (star!=0 and star != 4)):
                    print('*  ', end='')
                elif (star == 4 and (line!=0 and line!=4)) or (line==4 and star!=4):
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if star == 0 or (line+1==star):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='S':
        for line in range(5):
            for star in range(5):
                if (star==0 and (line!=0 and line!=4)) or(line==0 and (star!=0 and star!=4)):
                    print('* ', end='')
                elif (star==4 and line==1) or (line==4 and (star!=0 and star!=4)):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        for line in range(4):
            for star in range(5):
                if (star==4 and line!=3) or (line==3 and (star!=0 and star!=4)) or (star==0 and line==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()
    elif letter=='T':
        for line in range(11):
            for star in range(5):
                if line == 0 or star == 2:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
        print()
    elif letter=='U':
        collumn = 11
        row = 5

        for line in range(4):
            for star in range(5):
                if star == 0 or star == 4:
                    print('*  ', end='')
                else:
                    print('   ', end='')
            print()

        for line in range(4):
            for star in range(5):
                if (star == 0 and line != 3) or (star == 4 and line != 3) or (line == 3 and (star != 0 and star != 4)):
                    print('*  ', end='')
                else:
                    print('   ', end='')

            print()
        print()
    elif letter=='V':
        for line in range(7):
            for star in range(13):
                if (line==star)or (star==12-line):
                    print('*', end='')
                else:
                    print(' ', end='')

            print()
        print()
    elif letter=='W':
        for line in range(7):
            for star in range(13*2-1):
                if (line==star)or (star==12-line) or (star==12+line) or (star==24-line):
                    print('*', end='')
                else:
                    print(' ', end='')

            print()
        print()
    elif letter=='X':
        for line in range(7):
            for star in range(7):
                if (star!=0 and line==star) or (star==6-line):
                    print('* ', end='')
                else:
                    print('  ', end='')

            print()
        print()
    elif letter=='Y':
        for line in range(5):
            for star in range(9):
                if (line==star)or (star==8-line):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        for line in range(3):
            for star in range(9):
                if star == 4:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        print()
    elif letter=='Z':
        collumn = 10
        row = 6

        print('* ' * row)

        for line in range(collumn):
            space_number = collumn - line - 1
            for space in range(space_number):
                print(' ', end='')

            for star in range(row):
                if star == 0 or line == collumn - 1:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
        print()

string_name = input().upper()

for i in string_name:
    if i==' ':
        print(' ')
        print()
    else:
        name(i)