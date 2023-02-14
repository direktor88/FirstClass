def begin():
    print('igra krestiki - noliki')
    print()
    for j in m:
        print(*j)
    print()
    global czsel1, czsel2
    #user1_data = {}
    #user2_data = {}
    player1 = input('vvedi imya  ')
    #user1_data['user'] = player1
    czsel1 = input('viberi krestik "x" ili nolik "o"  ')  # CrossZeroSelection
    #user1_data['simvol'] = czsel1
    player2 = input('vtoroi igrok vvedi imya ')
    #user2_data['user'] = player2
    if czsel1 == 'x':
        czsel2 = "o"
    else:
        czsel2 = "x"
    #user2_data['simvol'] = czsel2
    print("____________________________________________")
    print(f'pervi igrok "{player1}" vibral "{czsel1}"')
    print(f' vtoromu igroku "{player2}" dostalsa "{czsel2}"')


m = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]  # just borned matrix ;)
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


def clear():  # clear matrix
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


def check_win():  # proverka viigrisha
    mm = (win1, win2, win3, win4,  # matrix in matrix
          win5, win6, win7, win8)
    for ff in mm:  # cheking!!!
        if cross == ff:

            print("krestiki viigrali!!!")
            pobeda()
        elif zero == ff:
            print("noliki viigrali!!!")
            pobeda()


def nichya():
    ze = cr = 0 # ze - zero, cr - cross
    for i in m:
        for j in i:
            if j == 'o':
                ze += 1             # summ of zero
            elif j == 'x':
                cr += 1                #summ of cross
    if ((ze == 5) and (cr == 4)) or ((ze == 4) and (cr == 5)): # see what a bigger?
        print('Voznikla nichya, nachnite novuyou igru')
        exit()


def pobeda():  # deistvia pri pobede
    print()
    print('pobeda!!!')
    print()
    print("END")
    print()
    clear()
    for j in m:
        print(*j)
    exit()


def input_z():  # #vvod indeksa
    global z
    z = int(input('vvedi nomer stolbca ot 1 do 3  '))
    if 1 <= z <= 3:
        return z
    else:
        print('bud vnimatelen! stolbcov vsego 3 ')
        input_z()


def input_y():  ##vvod indeksa
    global y
    y = int(input('vvedi nomer stroki  '))
    if 1 <= y <= 3:
        return y
    else:
        print('bud vnimatelen! strok vsego 3 ')
        input_y()


def base_game():
        print()
        print("ХОД")
        print()
        input_z()  # vvod indeksa
        input_y()  # vvod indeksa
        val = str(input('vvedi simvol   '))
        # proverka ocheredi
        if cross[y][z] == "w":
            print("uzhe zanyto, viberi druguiu kletku")
        elif zero[y][z] == 'w':
            print("uzhe zanyto, viberi druguiu kletku")
        else:
            m[y][z] = val
            for j in m:
                print(*j) # print of result
            if m[y][z] == "x":  # create cross - zero matrix
                cross[y][z] = "w"
            elif m[y][z] == "o":
                zero[y][z] = "w"
            nichya()
            check_win()



begin()
base_game()
