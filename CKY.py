from gramatica import Gramatica

class CKY:
    def __init__(self, gramatica):
        self.gramatica = gramatica
    
    def pertany(self, paraula):
        n = len(paraula)
        taula = [[set() for _ in range(n)] for _ in range(n)]

        
        for i in range(n):
            lletra = paraula[i]
            taula[i][i] = self.gramatica.trobar_cap([lletra])
        
        for i in range(1,n):
            for j in range(n-i):
                columna = j+i
                for k in range(i):
                    primera = taula[j][columna-i+k]                
                    segona = taula[j+k+1][columna]
                    taula[j][columna].update(self.gramatica.trobar_combinacions(primera, segona))

        return self.gramatica.simbol_inicial in taula[0][n-1]