#teste navi capital Q1
# Adriano Tackano Amadio adriano.t.amadio@gmail.com
cont=0
for i in range (1,5001):
    a=float(i/49)
    a_int= int(i/49)
    b=float(i/37)
    b_int= int(i/37)
    par=float(i/2)
    par_int= int(i/2)
    
    a_dec= float(a-a_int)
    b_dec= float(b-b_int)
    par_dec= float(par-par_int)
    if a_dec==0 and b_dec==0 and par_dec==0:
        cont+=1
        print(i)
print("Há ", cont, "números pares multiplos de 49 e 37" )


