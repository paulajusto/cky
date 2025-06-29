from pytokr import item, items
from CKY import CKY
from gramatica import Gramatica

interactiu = False
gramatica = Gramatica()
num = 1
for i in items():

    if i != 'paraules':
        t = int(item())
        for j in range(t):
            gramatica.afegir_regla(i,list(item()))
        
    else:
        print('*******************************  ', num, '  *******************************')
        print(gramatica)
        gramatica.convertir_cnf(interactiu)

        cky = CKY(gramatica)
        num_p = int(item())

        for j in range(num_p):
            paraula = item()
            pertenyer = cky.pertany(paraula)
            if pertenyer:
                resposta = 'SI'
            else:
                resposta = 'NO'
            print(f'La paraula {paraula} {resposta} pertany a la gramàtica.')
        print()
        gramatica = Gramatica()
        num += 1

        

