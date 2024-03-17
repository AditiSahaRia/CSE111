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
    elif letter=='E':
        for line in range(11):
            for star in range(5):
                if (star == 0 and (line != 0 or line != 10)) or (line == 0 and star != 0) or (
                        line == 10 and star != 0) or (line == 5 and star < 4):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    elif letter=='F':
        for line in range(11):
            for star in range(5):
                if star == 0 or line == 0 or (line == 5 and star < 4):
                    print('* ', end='')
                else:
                    print('  ', end='')
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
    elif letter=='H':
        for line in range(11):
            for star in range(5):
                if star == 0 or star == 4 or line == 5:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
    elif letter=='I':
        for line in range(11):
            for star in range(5):
                if line == 0 or line == 10 or star == 2:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
    #elif letter=='J':
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
    #elif letter=='O':
    #elif letter=='P':
    #elif letter=='Q':
    #elif letter=='R':
    #elif letter=='S':
    elif letter=='T':
        for line in range(11):
            for star in range(5):
                if line == 0 or star == 2:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print('')
    #elif letter=='U':
    #elif letter=='V':
    #elif letter=='W':
    #elif letter=='X':
    #elif letter=='Y':
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

string_name = input().upper()

for i in string_name:
    if i=='C' or i=='J' or (i>='O' and i<='S') or (i>='U' and i<='Y'):
        print('Sorry, this letter is not available at this moment')
    else:
        name(i)