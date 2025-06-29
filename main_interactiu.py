from pytokr import item, items
from CKY import CKY
from gramatica import Gramatica
from CKY_probabilistic import CKY_Probabilistic
from gramatica_probabilistic import Gramatica_Probabilistic

interactiu = True
while True:
    try:
        i = int(input('Escull un algoritme: CKY (1) o CKY Probabilístic (2): '))
        if i in [1, 2]:
            break
        else:
            print("Només es poden escollir les opcions 1 (per l'Algoritme CKY) o 2 (per l'Algoritme CKY Probabilístic).")
    except ValueError:
        print("Has d'introduir un número (1 - Algoritme CKY o 2 - Algoritme CKY Probabilístic).")

def demanar_enter(missatge):
        while True:
            try:
                valor = int(input(missatge))
                if valor > 0:
                    return valor
                else:
                    print("El número ha de ser major que zero.")
            except ValueError:
                print("Entrada no vàlida. Introdueix un número enter positiu.")

def demanar_no_terminal(missatge):
    while True:
        k = input(missatge).strip()
        if k and k.isupper():
            return k
        else:
            print("Entrada no vàlida. El no terminal ha de contenir només lletres majúscules, dígits o guions baixos (ex: S, Z_2, ABC1).")

if i == 1:
    print('\n\033[1mALGORITME CKY\033[0m\n')
    gramatica = Gramatica()

    print("Indica quants símbols no terminals diferents tindrà la gramàtica, és a dir, quants 'caps' de produccions (a l'esquerra de la fletxa →) vols definir.\nEl primer símbol no terminal que escolleixis serà el teu símbol inicial.\n")
    t = demanar_enter('Nombre de símbols no terminals: ')

    for j in range(t):
        k = demanar_no_terminal(f'No terminal ({j+1}/{t}): ')
        print(f"\nIndica quantes produccions tindrà el símbol no terminal {k}.")
        l = demanar_enter('Nombre de produccions: ')
        produccions = []
        for m in range(l):
            print('\nSi vols que la producció sigui la paraula buida cal escriure: ε')
            n = input(f'Producció ({m+1}/{l}): ')
            produccions.append(n)
            gramatica.afegir_regla(k, list(n))
        print(f"\nRegla de producció {k} → {' | '.join(''.join(r) for r in produccions)} s'ha afegit a la gramàtica.\n")

    print('Gramàtica creada correctament.')
    print(gramatica)

    input("Prem Enter per verificar si la gramàtica està en CNF...\n")

    gramatica.convertir_cnf(interactiu)
    cky = CKY(gramatica)

    v = input('Vols comprovar si una paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()
    while v not in ['Y', 'N']:
        print("Resposta no vàlida. Introdueix 'Y' per sí o 'N' per no.")
        v = input('Vols comprovar si una paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()

    while v == 'Y':
        p = input('Paraula: ')
        print(f'La paraula {p} {"SI" if cky.pertany(p) else "NO"} pertany a la gramàtica.')
        v = input('Vols comprovar si una altra paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()
        while v not in ['Y', 'N']:
            print("Resposta no vàlida. Introdueix 'Y' per sí o 'N' per no.")
            v = input('Vols comprovar si una altra paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()

elif i == 2:
    print('\n\033[1mALGORITME CKY PROBABILÍSTIC\033[0m\n')
    gramatica = Gramatica_Probabilistic()

    print("Indica quants símbols no terminals diferents tindrà la gramàtica, és a dir, quants 'caps' de produccions (a l'esquerra de la fletxa →) vols definir.\nEl primer símbol no terminal que escolleixis serà el teu símbol inicial.\n")
    t = demanar_enter('Nombre de símbols no terminals: ')
    
    def demanar_probabilitat(missatge):
        while True:
            try:
                p = float(input(missatge))
                if 0.0 <= p <= 1.0:
                    return p
                else:
                    print("La probabilitat ha d'estar entre 0 i 1.")
            except ValueError:
                print("Entrada no vàlida. Introdueix un número decimal entre 0 i 1.")

    for j in range(t):
        k = demanar_no_terminal(f'No terminal ({j+1}/{t}): ')
        print(f"\nIndica quantes produccions tindrà el símbol no terminal {k}.")
        l = demanar_enter('Nombre de produccions: ')
        produccions = []
        for m in range(l):
            print('\nSi vols que la producció sigui la paraula buida cal escriure: ε')
            n = input(f'Regla ({m+1}/{l}): ')
            produccions.append(n)
        p = demanar_probabilitat(f'Probabilitat de la regla {k} → {" ".join(produccions)}: ')
        print(f"\nRegla de producció {k} → {' | '.join(''.join(r) for r in produccions)} s'ha afegit a la gramàtica amb probabilitat {p}.\n")
        gramatica.afegir_regla(k, produccions, p)
    
    print('Gramàtica creada correctament.')
    print(gramatica)
    cky = CKY_Probabilistic(gramatica)

    v = input('Vols comprovar si una paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()
    while v not in ['Y', 'N']:
        print("Resposta no vàlida. Introdueix 'Y' per sí o 'N' per no.")
        v = input('Vols comprovar si una paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()

    while v == 'Y':
        p = input('Paraula: ')
        pertenyer, probabilitat = cky.pertany(p)
        if pertenyer and probabilitat:
            resposta = 'SI'
            print(f'La paraula {p} {resposta} pertany a la gramàtica amb una probabilitat de {probabilitat}.')
        else:
            resposta = 'NO'
            print(f'La paraula {p} {resposta} pertany a la gramàtica.')
        v = input('Vols comprovar si una altra paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()
        while v not in ['Y', 'N']:
            print("Resposta no vàlida. Introdueix 'Y' per sí o 'N' per no.")
            v = input('Vols comprovar si una altra paraula pertany a aquesta gramàtica? (Y/N): ').strip().upper()