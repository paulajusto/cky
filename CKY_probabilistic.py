from gramatica_probabilistic import Gramatica_Probabilistic
from CKY import CKY

class CKY_Probabilistic(CKY):
    def __init__(self, gramatica):
        self.gramatica = gramatica
    
    def pertany(self, paraula):
        n = len(paraula)
        taula = [[set() for _ in range(n)] for _ in range(n)]

        
        for i in range(n):
            lletra = paraula[i]
            caps = self.gramatica.trobar_cap([lletra])
            for cap in caps:
                taula[i][i].add((cap, self.gramatica.trobar_probabilitat(cap,[lletra])))
        

        for i in range(1,n):
            for j in range(n-i):
                columna = j+i
                for k in range(i):
                    primera = taula[j][columna-i+k]                
                    segona = taula[j+k+1][columna]
                    if primera and segona:
                        taula[j][columna].update(self.gramatica.trobar_combinacions(primera, segona))
        prob = 0
        pertany = False
        for lletra, proba in taula[0][n-1]:
            if lletra == self.gramatica.simbol_inicial:
                prob = max(prob, proba)
                pertany = True

        return pertany, prob