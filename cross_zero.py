#  a,b,c
#  d,e,f
#  g,h,i
# a,b,c; a.e.i; a,d,g; d,c,f; g,h,i; c.e.g; b,e,h; e,f.i win position

matrix={} #dict

def sel (); # cross or zero
    #wrapper
    print('select cross or zero: 0 or x' )
    a = input()
    if a == "0" or "x";
        print "vvedi snachala stroku a zatem stolbec " 
        stroka=input('vvedi stroku 1-3   ')
        kolonka=input('vvedi kolonku 1-3   ')
        return a, stroka, kolonka
    else sel()

    



#select cross or zero
cross=input('vvedi krestik   ')


zero=input('vvedi nolik   ')
# chto vvedeno?

stroka=input('vvedi stroku 1-3   ')
kolonka=input('vvedi kolonku 1-3   ')
c=matrix[0]
y=matrix[1]
z=matrix[2]
if stroka == int('1');
    
