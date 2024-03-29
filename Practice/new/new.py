cache = {}
def buildCache():
    a = [
        "  #  ",
        " # # ",
        "#####",
        "#   #",
        "#   #",
    ]
    cache[0] = a
    b = [
        "#### ",
        "#   #",
        "#####",
        "#   #",
        "#####"
    ]
    cache[1] = b
    c = [
        "#####",
        "#   #",
        "#    ",
        "#   #",
        "#####"
    ]
    cache[2] = c
    d = [
        "###  ",
        "#  # ",
        "#   #",
        "#  # ",
        "###  "
    ]
    cache[3] = d
    e = [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#####"
    ]
    cache[4] = e
    f = [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#    ",
    ]
    cache[5] = f
    g = [
        "####",
        "#   #",
        "# ###",
        "# # #",
        "####"
    ]
    cache[6] = g
    h = [
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
    ]
    cache[7] = h
    i = [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####"
    ]
    cache[8] = i
    j = [
        "#####",
        "    #",
        "    #",
        " #  #",
        " ### "
    ]
    cache[9] = j
    k = [
        "#  # ",
        "# #  ",
        "#    ",
        "# #  ",
        "#  # "
    ]
    cache[10] = k
    l = [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ]
    cache[11] = l
    m = [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #"
    ]
    cache[12] = m
    n = [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #"
    ]
    cache[13] = n
    o = [
        "  ##  ",
        "##  ##",
        "##  ##",
        "##  ##",
        "  ##  "
    ]
    cache[14] = o
    p = [
        "#### ",
        "#   #",
        "#### ",
        "#    ",
        "#    "
    ]
    cache[15] = p
    q = [
        "  ##  ",
        "##  ##",
        "##  ##",
        "  ##  ",
        "    # ",
    ]
    cache[16] = q
    r = [
        "#### ",
        "#   #",
        "#### ",
        "# #  ",
        "#  # "
    ]
    cache[17] = r
    s = [
        " ### ",
        "#    ",
        "#### ",
        "    #",
        " ### "
    ]
    cache[18] = s
    t = [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  "
    ]
    cache[19] = t
    u = [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ]
    cache[20] = u
    v = [
        "#       #",
        " #     # ",
        "  #   #  ",
        "   # #   ",
        "    #    "
    ]
    cache[21] = v
    w = [
        "#   #   #",
        "#   #   #",
        " # # # # ",
        " # # # # ",
        "  #   #  "
    ]
    cache[22] = w
    x = [
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #"
    ]
    cache[23] = x
    y = [
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  "
    ]
    cache[24] = y
    z = [
        "#####",
        "   # ",
        "  #  ",
        " #   ",
        "#####"
    ]
    cache[25] = z


def printString(str):
    output = ""
    str = str.upper()
    for i in range(5):
        for x in str:
            if x==' ':
                output += '   '
                continue
            else:
                val = ord(x) - 65
                output += cache[val][i] + " "
        output += "\n"
    print(output)

buildCache()
y = input()
printString(y)