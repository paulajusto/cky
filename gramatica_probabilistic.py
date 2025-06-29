from gramatica import Gramatica

class Gramatica_Probabilistic(Gramatica):
    
    def __init__(self):
        super().__init__()
    
    def _existeix_regla(self, cap, cos):
        if self._existeix_cap(cap):
            for dreta in self.dicc[cap]:
                if cos == dreta[0]:
                    return True
        return False

    def trobar_cap(self, cos):
        caps = set()
        for cap, dreta in self.dicc.items():
            for produccions in dreta:
                if cos == produccions[0]:
                    caps.add(cap) 
        return caps 
    
    def trobar_probabilitat(self, cap, cos):
        if self._existeix_cap(cap):
            for produccio in self.dicc[cap]:
                    if cos == produccio[0]:
                        return produccio[1]

    def afegir_regla(self, cap, cos, prob):
        if not self._existeix_regla(cap, cos):
            if self._existeix_cap(cap):
                self.dicc[cap].append((list(cos), prob))
            else:
                self.dicc[cap] = [(list(cos), prob)]
    
    def trobar_combinacions(self, primera, segona):
        resp = set()
        for (pri,prob_pri) in primera:
            for (seg, prob_seg) in segona:
                caps = self.trobar_cap([pri]+[seg])
                for cap in caps:
                    probabilitat = prob_pri * prob_seg * self.trobar_probabilitat(cap,[pri]+[seg])
                    resp.add((cap, probabilitat))
        return resp

    def _es_cnf(self):
        pass
    def convertir_cnf(self):
        pass

    def __str__(self):
        resultat = '\nGramàtica:\n'
        for cap, cos in self.dicc.items():
            resultat += f'{cap} → '
            produccions = [' '.join(produccio[0])+' ('+str(produccio[1])+')' for produccio in cos]
            resultat += ' | '.join(produccions)
            resultat += '\n'
        return resultat
