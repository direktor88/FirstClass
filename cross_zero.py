#  a,b,c
#  d,e,f
#  g,h,i
# a,b,c; a.e.i; a,d,g; d,c,f; g,h,i; c.e.g; b,e,h; e,f.i win position
print ('igra krestiki - noliki')
print()
user1_data={}
user2_data={}
player1 = input('vvedi imya  ')
user1_data['user']=player1
czsel1 = input('viberi krestik "x" ili nolik "o"  ')#CrossZeroSelection
user1_data['simvol']=czsel1
player2 = input ('vtoroi igrok vvedi imya ')
user2_data['user']=player2
if czsel1=='x':
    czsel2="o"
else:
    czsel2="x"
user2_data['simvol']=czsel2
#print(user1_data,user2_data)

print("____________________________________________")
print (f'pervi igrok "{player1}" vibral "{czsel1}"')
print (f' vtoromu igroku "{player2}" dostalsa "{czsel2}"')
m=[
   [0,1,2,3],
   [1,0,0,0],
   [2,0,0,0],
   [3,0,0,0]
]
def chkwin (): # Check win
    if m[1][1] and m[1][2] and m[1][3] =='x' or 'o':
        print('win')
    elif m[1][1] and m[2][2] and m[3][3] =='x' or 'o':
        print('win')
    elif m[1][1] and m[2][1] and m[3][1] =='x' or 'o':
        print('win')
    elif m[1][2] and m[2][2] and m[3][2] =='x' or 'o':
        print('win')
    elif m[1][3] and m[2][3] and m[3][3] =='x' or 'o':
        print('win')
    elif m[2][1] and m[2][2] and m[2][3] =='x' or 'o':
        print('win')
    elif m[3][1] and m[3][2] and m[3][3] =='x' or 'o':
        print('win')
    elif m[3][1] and m[2][2] and m[1][3] =='x' or 'o':
        print('win')
print('-----')
# def userchk ():
def simvol_chk ():
    if m[x][z]=="x" or "o":
def base_game ():
    for i in range (9): # all step = 9
        z=int(input('vvedi stolbec  '))
        x=int(input('vvedi stroku  '))
        val=input('vvedi simvol  ')
        # функция проверки введенного символа
        # def проверка занятой ячейки
        m[x][z]=val
        simvol_chk()
        for i in m:
            print(i, sep='\n' )
        # def  проверка
        if chkwin():
            print ('pobeda')
            break
        if i==9:
            print('konec')




    









    
