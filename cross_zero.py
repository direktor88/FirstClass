#  a,b,c
#  d,e,f
#  g,h,i
# a,b,c; a.e.i; a,d,g; d,c,f; g,h,i; c.e.g; b,e,h; e,f.i win position
print ('igra krestiki - noliki')
print()
player1 = input('vvedi imya  ')
czsel1 = input('viberi krestik "x" ili nolik "o"  ') #CrossZeroSelection
player2 = input ('vtoroi igrok vvedi imya ')
if czsel1=='x':
    czsel2="o"
else:
    czsel2="x"
print()
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
        #print('win')
    elif m[1][1] and m[2][2] and m[3][3] =='x' or 'o':
        #print('win')
    elif m[1][1] and m[2][1] and m[3][1] =='x' or 'o':
        #print('win')
    elif m[1][2] and m[2][2] and m[3][2] =='x' or 'o':
        #print('win')
    elif m[1][3] and m[2][3] and m[3][3] =='x' or 'o':
        #print('win')
    elif m[2][1] and m[2][2] and m[2][3] =='x' or 'o':
        #print('win')
    elif m[3][1] and m[3][2] and m[3][3] =='x' or 'o':
        #print('win')
    elif m[3][1] and m[2][2] and m[1][3] =='x' or 'o':
        #print('win')



# нужно прописать зависимость
# https://lms.skillfactory.ru/courses/course-v1:SkillFactory+FPW-2.0+27AUG2020/courseware/5474bc39c2294893840f3e89e37d31db/c9591776961d497bbeb9bad8c5e41685/3?activate_block_id=block-v1%3ASkillFactory%2BFPW-2.0%2B27AUG2020%2Btype%40vertical%2Bblock%40be2d1081789d4a98a9a670f01557594b
print('-----')

# def userchk ():


for i in range (9): # all step = 9
    z=int(input('vvedi stolbec  '))
    x=int(input('vvedi stroku  '))
    val=input('vvedi simvol  ')
    # функция проверки введенного символа
    # def проверка занятой ячейки
    m[x][z]=val
    for i in m:
        print(i, sep='\n' )

    # def  проверка
    chkwin()
    if chkwin():
        print ('pobeda')
        break
    if i==9:
        print('konec')




    









    
