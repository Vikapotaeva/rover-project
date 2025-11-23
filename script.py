a = [["*" for i in range(8)] for j in range(8)]
a[0][6] = "m"
a[5][4] = "s1"
a[4][5] = "s2"
a[3][7] = "l"
a[1][3] = "p"
a[6][2] = "k"
a[7][7] = "v"
x = y = 0
hp = 3
mech = zelie = key = 0
a1 = [[" " for i in range(8)] for j in range(8)]

while x != 7 and y != 7:
    if x != 0 and y != 0:
        print(*a1)
        print("жизни: ", hp)
        print("меч: ", mech)
        print("зелье: ", zelie)
    x1 = int(input("вниз(0 или 1) "))
    y1 = int(input("вправо(0 или 1) "))
    x += x1
    y += y1
    if hp == 0:
        print("Вы проиграли")
        break
    if x == 7 and y == 7:
        if key == 0:
            print("вы проиграли")
            break
        else:
            print("Вы выиграли")
            break
    if x == 0 and y == 6:
        a1[0][6] = "m"
        if mech == 0:
            hp -= 1
        else:
            mech = 0

    elif x == 5 and y == 4:
        a1[5][4] = "s1"
        mech = 1

    elif x == 4 and y == 5:
        a1[4][5] = "s2"
        zelie = 1

    elif x == 3 and y == 7:
        a1[3][7] = "l"
        if zelie == 0:
            hp -= 1
        else:
            zelie = 0

    elif x == 1 and y == 3:
        a1[1][3] = "p"
        if key == 0:
            a[6][2] = k
            key = 1

    elif x == 6 and y == 2:
        a1[6][2] = "k"
        key = 1

    else: a1[x][y] = "*"







