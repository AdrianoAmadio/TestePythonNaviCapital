#teste navi capital Q2
# Adriano Tackano Amadio adriano.t.amadio@gmail.com
import numpy as np
x=np.zeros(10)

for i in range (10):
    if (i%2)==0:
        x[i]=(3**(i))+7*np.math.factorial(i)
    else:
        x[i]=(2**(i))+4*np.log(i)
#print(x)
pos_do_max = np.argmax(x) #lembre-se que começamos a contar do zero.
print("O máximo ocorre na posição", pos_do_max, "do vetor x")
print("lembre-se que começamos a contar do zero.")
print("A média dos valores de x é:",np.round(np.mean(x),decimals=2))