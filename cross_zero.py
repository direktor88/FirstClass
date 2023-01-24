def begin():
    print('igra krestiki - noliki')
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
] # just borned matrix ;)
win1 = [ # win combination
    [0, 1, 2, 3],
    [1, 'x', '_', '_'],
    [2, 'x', '_', '_'],
    [3, 'x', '_', '_']
]
win2 = [
    [0, 1, 2, 3],
    [1, 'x', 'x', 'x'],
    [2, '_', '_', '_'],
    [3, '_', '_', '_']
]
win3 = [
    [0, 1, 2, 3],
    [1, 'x', '_', '_'],
    [2, '_', 'x', '_'],
    [3, '_', '_', 'x']
]
win4 = [
    [0, 1, 2, 3],
    [1, '_', 'x', '_'],
    [2, '_', 'x', '_'],
    [3, '_', 'x', '_']
]
win5 = [
    [0, 1, 2, 3],
    [1, '_', '_', 'x'],
    [2, '_', '_', 'x'],
    [3, '_', '_', 'x']
]
win6 = [
    [0, 1, 2, 3],
    [1, '_', '_', 'x'],
    [2, '_', 'x', '_'],
    [3, 'x', '_', '_']
]
win7 = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, 'x', 'x', 'x'],
    [3, '_', '_', '_']
]
win8 = [
    [0, 1, 2, 3],
    [1, '_', '_', '_'],
    [2, '_', '_', '_'],
    [3, 'x', 'x', 'x']
]
def clear():
    global m
    m =  [
        [0, 1, 2, 3],
        [1, '_', '_', '_'],
        [2, '_', '_', '_'],
        [3, '_', '_', '_']
    ]


def pobeda():
    print()
    print('pobeda!!!')
    print ()
    print("END")
    print()
    clear()
    for j in m:
        print(*j)
    print()
    begin()


#
def simvol_chk():
    if m[x][z] == 0:
        # base_game()
        print("uzhe zanyto, viberi druguiu kletku")


def base_game():
    for i in range(9):  # all step = 9
        print()
        print(i + 1, "ХОД")
        global x, z  # meet
        print()
        z = int(input('vvedi stolbec  '))
        x = int(input('vvedi stroku  '))
        val = str(input('vvedi simvol  '))
        print()
        # функция проверки введенного символа
        # def проверка занятой ячейки

        m[x][z] = val
        for j in m:
            print(*j)
        mm = (win1, win2, win3, win4, # matrix in matrix
              win5, win6, win7, win8)
        for ff in mm: # cheking!!!
            if m == ff:
                pobeda()
              # if m == win1:
        #     pobeda()
        # elif m == win2:
        #     pobeda()
        # elif m == win3:
        #     pobeda()
        # elif m == win4:
        #     pobeda()
        # elif m == win5:
        #     pobeda()
        # elif m == win6:
        #     pobeda()
        # elif m == win7:
        #     pobeda()
        # elif m == win8:
        #     pobeda()

begin()
base_game()
