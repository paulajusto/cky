from pytokr import item, items
from CKY_probabilistic import CKY_Probabilistic
from gramatica_probabilistic import Gramatica_Probabilistic

gramatica = Gramatica_Probabilistic()
num = 1
for i in items():

    if i != 'paraules':
        t = int(item())
        produccio = []
        for j in range(t):
            produccio.append(item())
        gramatica.afegir_regla(i,produccio, float(item()))
        
    else:
        print('*******************************  ', num, '  *******************************')
        print(gramatica)

        cky = CKY_Probabilistic(gramatica)
        num_p = int(item())

        for j in range(num_p):
            paraula = item()
            pertenyer, probabilitat = cky.pertany(paraula)
            if pertenyer and probabilitat:
                resposta = 'SI'
                print(f'La paraula {paraula} {resposta} pertany a la gramàtica amb una probabilitat de {probabilitat}.')

            else:
                resposta = 'NO'
                print(f'La paraula {paraula} {resposta} pertany a la gramàtica.')
        print()
        gramatica = Gramatica_Probabilistic()
        num += 1
                

    
        
        