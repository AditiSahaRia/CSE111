cache = []
def buildCache():
    a = [
        "  #  ",
        " # # ",
        "#####",
        "#   #",
        "#   #",
    ]
    cache.append(a)
    b = [
        "#### ",
        "#   #",
        "#####",
        "#   #",
        "#####"
    ]
    cache.append(b)
    c = [
        "#####",
        "#   #",
        "#    ",
        "#   #",
        "#####"
    ]
    cache.append(c)
    d = [
        "###  ",
        "#  # ",
        "#   #",
        "#  # ",
        "###  "
    ]
    cache.append(d)
    e = [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#####"
    ]
    cache.append(e)
    f = [
        "#####",
        "#    ",
        "#####",
        "#    ",
        "#    ",
    ]
    cache.append(f)
    g = [
        "####",
        "#   #",
        "# ###",
        "# # #",
        "####"
    ]
    cache.append(g)
    h = [
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
    ]
    cache.append(h)
    i = [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####"
    ]
    cache.append(i)
    j = [
        "#####",
        "    #",
        "    #",
        " #  #",
        " ### "
    ]
    cache.append(j)
    k = [
        "#  # ",
        "# #  ",
        "#    ",
        "# #  ",
        "#  # "
    ]
    cache.append(k)
    l = [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ]
    cache.append(l)
    m = [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #"
    ]
    cache.append(m)
    n = [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #"
    ]
    cache.append(n)
    o = [
        "  ##  ",
        "##  ##",
        "##  ##",
        "##  ##",
        "  ##  "
    ]
    cache.append(o)
    p = [
        "#### ",
        "#   #",
        "#### ",
        "#    ",
        "#    "
    ]
    cache.append(p)
    q = [
        "  ##  ",
        "##  ##",
        "##  ##",
        "  ##  ",
        "    # ",
    ]
    cache.append(q)
    r = [
        "#### ",
        "#   #",
        "#### ",
        "# #  ",
        "#  # "
    ]
    cache.append(r)
    s = [
        " ### ",
        "#    ",
        "#### ",
        "    #",
        " ### "
    ]
    cache.append(s)
    t = [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  "
    ]
    cache.append(t)
    u = [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ]
    cache.append(u)
    v = [
        "#       #",
        " #     # ",
        "  #   #  ",
        "   # #   ",
        "    #    "
    ]
    cache.append(v)
    w = [
        "#   #   #",
        "#   #   #",
        " # # # # ",
        " # # # # ",
        "  #   #  "
    ]
    cache.append(w)
    x = [
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #"
    ]
    cache.append(x)
    y = [
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  "
    ]
    cache.append(y)
    z = [
        "#####",
        "   # ",
        "  #  ",
        " #   ",
        "#####"
    ]
    cache.append(z)


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