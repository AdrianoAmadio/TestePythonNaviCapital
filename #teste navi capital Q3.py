#teste navi capital Q3
# Adriano Tackano Amadio adriano.t.amadio@gmail.com
import numpy as np
nomes=[]
notas=[]
tabela=[nomes, notas]
print("Digite as notas com ponto como separador e não vírgula!")
for i in range (5):
    nomes.append(str(input("Digite o nome do aluno:")))
    notas.append(float(input("Digite a nota:"))) 

indice_max= np.argmax(notas)
print("O aluno com maior nota foi:",nomes[indice_max],"com a nota de:",notas[indice_max])