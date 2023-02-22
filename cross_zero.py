def begin():
    print('igra krestiki - noliki')
    print()
    for j in m:
        print(*j)
    print()
    global czsel1, czsel2, player1, player2
    player1 = input('vvedi imya  ')
    input_cz()
    czsel1 = val
    player2 = input('vtoroi igrok vvedi imya ')
    if czsel1 == 'x':
        czsel2 = "o"
    else:
        czsel2 = "x"
    print("____________________________________________")
    print(f'pervi igrok "{player1}" vibral "{czsel1}"')
    print(f' vtoromu igroku "{player2}" dostalsa "{czsel2}"')


def input_cz():
    global val
    val = input('nazhmi krestik "x" ili nolik "o"  ')
    if val == 'x' or val == 'o':
        return val
    else:
        print('nevernii vibor')
        input_cz()


m = [  # base matrix
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
cross = [  # clear matrix for "cross"
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
zero = [  # clear matrix for "zero"
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
win1 = [  # win combination
    [0, 1, 2, 3],
    [1, 'w', '_', '_'],
    [2, 'w', '_', '_'],
    [3, 'w', '_', '_']
]
win2 = [
    [0, 1, 2, 3],
    [1, 'w', 'w', 'w'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
win3 = [
    [0, 1, 2, 3],
    [1, 'w', '_', '_'],
    [2, '_', 'w', '_'],
    [3, '_', '_', 'w']
]
win4 = [
    [0, 1, 2, 3],
    [1, '_', 'w', '_'],
    [2, '_', 'w', '_'],
    [3, '_', 'w', '_']
]
win5 = [
    [0, 1, 2, 3],
    [1, '_', '_', 'w'],
    [2, '_', '_', 'w'],
    [3, '_', '_', 'w']
]
win6 = [
    [0, 1, 2, 3],
    [1, '_', '_', 'w'],
    [2, '_', 'w', '_'],
    [3, 'w', '_', '_']
]
win7 = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, 'w', 'w', 'w'],
    [3, '_', '_', '_']
]
win8 = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, 'w', 'w', 'w']
]


def clear():  # clear all matrix
    global m, zero, cross
    m = [
        [0, 1, 2, 3],
        [1, '_', '_', '_'],
        [2, '_', '_', '_'],
        [3, '_', '_', '_']
    ]
    cross = [  # clear matrix for "cross"
        [0, 1, 2, 3],
        [1, '_', '_', '_'],
        [2, '_', '_', '_'],
        [3, '_', '_', '_']
    ]
    zero = [  # clear matrix for "zero"
        [0, 1, 2, 3],
        [1, '_', '_', '_'],
        [2, '_', '_', '_'],
        [3, '_', '_', '_']
    ]


def check_win():  # proverka viigrisha (check winner)
    mm = (win1, win2, win3, win4,  # create matrix in matrix
          win5, win6, win7, win8)
    for ff in mm:  # cheking!!!
        if cross == ff:
            cross_win()
        elif zero == ff:
            zero_win()

def zero_win():
    if czsel1 == 'o':
        print()
        print(f'igrok {player1} viigral')
        pobeda()
    elif czsel2 == 'o':
        print()
        print(f'igrok {player2} viigral')
        pobeda()

def cross_win():
    if czsel1 == 'x':
        print()
        print(f'igrok {player1} viigral')
        pobeda()
    elif czsel2 == 'x':
        print()
        print(f'igrok {player2} viigral')
        pobeda()


def nichya():  #when we stop game
    ze = cr = 0  # ze - zero, cr - cross
    for i in m:
        for j in i:
            if j == 'o':
                ze += 1  # summ of zero
            elif j == 'x':
                cr += 1  # summ of cross
    if ((ze == 5) and (cr == 4)) or ((ze == 4) and (cr == 5)):  # see what a bigger?
        print('Voznikla nichya, nachnite novuyou igru')
        clear()
        begin()
        base_game()
        # exit() # if need


def pobeda():  # deistvia pri pobede
    print()
    print("END")
    print()
    for j in m:
        print(*j)
    # clear()
    exit()


def input_z():  # input coordinates
    global z
    z = int(input('vvedi nomer stolbca ot 1 do 3  '))
    if 1 <= z <= 3:
        return z
    else:
        print('bud vnimatelen! stolbcov vsego 3 ')
        input_z()


def input_y():  # input number of row
    global y
    y = int(input('vvedi nomer stroki  '))
    if 1 <= y <= 3:
        return y
    else:
        print('bud vnimatelen! strok vsego 3 ')
        input_y()


# def ochered ():
#     if (count + 2) % 2 == 0 and val == czsel1:
#         #if val == czsel1:
#         print('est sovpadenie')
#     else:
#         print('ne vernii simvol')
# ochered()
#     elif (count + 2) % 2 == 1:
#         if val == czsel2:
#             print('kto to poshel ne v svoyou ochered')


def base_game():
    global count
    count = int(1)
    while count <= 9:
        print()
        for j in m:  # print matrix of cross zero
            print(*j)
        print()
        print(f'ХОД {count}')
        print()
        input_z()  # vvod indeksa
        input_y()  # vvod indeksa
        input_cz()  # input cross or zero
        # proverka ocheredi

        # if (count + 2) % 2 != 0 and val != czsel1:
        # game

        # elif (count + 2) % 2 == 1 and val == czsel2:
        # game
        #
        # else:
        # print('dolzhen bit drugoi simvol, ili ochered ne ta')
        # base_game()

        if cross[y][z] == "w" or zero[y][z] == 'w':  # check clear cell of matrix
            print()
            print("!!! AUCHTUNG !!! uzhe zanyto, viberi druguiu kletku")
        else:
            m[y][z] = val
            if m[y][z] == "x":  # create cross - zero matrix
                cross[y][z] = "w"
            elif m[y][z] == "o":
                zero[y][z] = "w"
            nichya()
            check_win()
            count += 1


begin()
base_game()
