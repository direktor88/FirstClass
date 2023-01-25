def begin():
    print('igra krestiki - noliki')
    print()
    for j in m:
        print(*j)
    print()
    user1_data = {}
    user2_data = {}
    player1 = input('vvedi imya  ')
    user1_data['user'] = player1
    czsel1 = input('viberi krestik "x" ili nolik "o"  ')  # CrossZeroSelection
    user1_data['simvol'] = czsel1
    player2 = input('vtoroi igrok vvedi imya ')
    user2_data['user'] = player2
    if czsel1 == 'x':
        czsel2 = "o"
    else:
        czsel2 = "x"
    user2_data['simvol'] = czsel2
    print("____________________________________________")
    print(f'pervi igrok "{player1}" vibral "{czsel1}"')
    print(f' vtoromu igroku "{player2}" dostalsa "{czsel2}"')


m = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]  # just borned matrix ;)
cross = [ # clear matrix for "cross"
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
zero = [ # clear matrix for "zero"
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


def clear(): # clear matrix
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


def check_win():
    mm = (win1, win2, win3, win4,  # matrix in matrix
          win5, win6, win7, win8)
    for ff in mm:  # cheking!!!
        if cross == ff:
            pobeda()
        elif zero ==ff:
            pobeda()


def pobeda():
    print()
    print('pobeda!!!')
    print()
    print("END")
    print()
    clear()
    for j in m:
        print(*j)
    print()
    # begin()


#
def simvol_chk():
    if m[x][z] == 0:
        # base_game()
        print("uzhe zanyto, viberi druguiu kletku")


def base_game():
    i = 0
    while i < 9:  # all step = 9
        print()
        print(i + 1, "ХОД")
        global y, z  # meeting
        print()
        z = int(input('vvedi stolbec  '))
        y = int(input('vvedi stroku  '))
        val = str(input('vvedi simvol  '))
        print()
        # функция проверки введенного символа
        # def проверка занятой ячейки
        m[y][z] = val
        for j in m:
            print(*j)
            # функция замены переменной в матрице.
        if m[y][z] == "x":  # create cross - zero matrix
            cross[y][z] = "w"
        elif m[y][z] == "o":
            zero[y][z] = "w"
        check_win()
        i = +1


begin()
base_game()
