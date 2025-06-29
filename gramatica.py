class Gramatica():
    def __init__(self, simbol_inicial = 'S'):
        self.dicc = {}
        self.simbol_inicial = simbol_inicial
        self.i = 1
    
    def _existeix_cap(self, cap):
        return cap in self.dicc
    
    def _existeix_regla(self, cap, cos):
        if self._existeix_cap(cap):
            return cos in self.dicc[cap]
        return False
    
    def __trobar_cos(self, cap):
        if self._existeix_cap(cap):
            return self.dicc[cap]

    def trobar_cap(self, cos):
        caps = set()
        for cap, dreta in self.dicc.items():
            if cos in dreta:
                caps.add(cap)
        return caps 

    def afegir_regla(self, cap, cos):
        if not self._existeix_regla(cap, cos):
            if self._existeix_cap(cap):
                self.dicc[cap].append(list(cos))
            else:
                self.dicc[cap] = [list(cos)]
    
    def _eliminar_regla(self, cap, cos):
        if self._existeix_regla(cap, cos):
            self.dicc[cap].remove(cos)


    def trobar_combinacions(self, primera, segona):
        caps = set()
        for cap, cos in self.dicc.items():
            for produccio in cos:
                if len(produccio) == 2 and produccio[0] in primera and produccio[1] in segona:
                    caps.add(cap)
        return caps
    
    def __eliminar_epsilon(self):
        caps = self.trobar_cap(['ε'])
        caps.discard(self.simbol_inicial)
        if not caps:
            return None
        for cap in caps:
            for produccions in self.__trobar_cos(cap):
                if 'ε' in produccions:
                    self._eliminar_regla(cap, produccions)
        
        noves_regles_buides = set()
        for cap, cos in self.dicc.items():
            i = 0
            while i < len(cos):
                for l in range(len(cos[i])):
                    if cos[i][l] in caps:
                        nova_prod = [x for y, x in enumerate(cos[i]) if y != l]
                        if len(nova_prod) >= 1:
                            self.afegir_regla(cap, nova_prod)
                        else:
                            noves_regles_buides.add(cap)
                i += 1
        
        if noves_regles_buides:
            for cap in noves_regles_buides:
                self.afegir_regla(cap, ['ε'])
            
            self.__eliminar_epsilon()

    def __eliminar_unitaries(self):
        items = list(self.dicc.items()) 
        for cap, cos in items:
            i = 0
            eliminades = set()
            while i < len(cos):
                if len(cos[i]) == 1 and cos[i][0].isupper():
                    if cap == cos[i][0]:
                        self._eliminar_regla(cap, cos[i][0])
                    if cos[i][0] not in eliminades:
                        eliminat = cos[i][0]
                        noves_prod = self.dicc[eliminat]
                        for dreta in noves_prod:
                            self.afegir_regla(cap,dreta)
                        eliminades.add(eliminat)
                i += 1
            for el in eliminades:
                self._eliminar_regla(cap, [el])

    def __substituir_terminals(self):
        terminals = set()
        for cap, cos in self.dicc.items():
            for produccio in range(len(cos)):
                if len(cos[produccio]) > 1:
                    for i in range(len(cos[produccio])):
                        if cos[produccio][i].islower():
                            terminals.add(cos[produccio][i])
                            self.dicc[cap][produccio][i] = f'T_{cos[produccio][i].upper()}'
        for t in terminals:
            self.afegir_regla(f'T_{t.upper()}', [t])

    def __descompondre_llargues(self):
        items = list(self.dicc.items()) 

        for cap, cos in items:
            for produccions in cos:
                if len(produccions) > 2:
                    nou_cap = f'Z_{self.i}'
                    self.i += 1
                    nou_cos = produccions[1:]
                    self.afegir_regla(nou_cap, nou_cos)
                    self.afegir_regla(cap, [produccions[0]]+[nou_cap])
                    self._eliminar_regla(cap, produccions)
        
        if not self._es_cnf():
            self.__descompondre_llargues()
    
    
    def _es_cnf(self):
        for cap, cos in self.dicc.items():
            for produccio in cos:
                if len(produccio) > 2:
                    return False
                elif len(produccio) == 2 and (produccio[0].islower() or produccio[1].islower() or self.simbol_inicial in produccio):
                    return False
                elif len(produccio) == 1: 
                    if produccio[0].isupper():
                        return False
                    if produccio[0] == 'ε' and cap != self.simbol_inicial:
                        return False
        return True
    
    def __nou_inicial(self):
        antic_inicial = self.simbol_inicial
        __nou_inicial = antic_inicial + antic_inicial
        self.afegir_regla(__nou_inicial, [antic_inicial])
        self.simbol_inicial = __nou_inicial
        if ['ε'] in self.__trobar_cos(antic_inicial):
            self.afegir_regla(__nou_inicial, ['ε'])

    def convertir_cnf(self, interactiu): 
        if self._es_cnf():
            print('La gramàtica està en CNF\n')
        
        else:
            print('La gramàtica NO està en CNF')
            
            if interactiu:
                input('\nPrem Enter per passar la gramàtica a CNF')

            self.__nou_inicial()
            self.__eliminar_epsilon()
            self.__eliminar_unitaries()
            self.__substituir_terminals()
            self.__descompondre_llargues()
            print(self)
            print('La gramàtica està en CNF\n')


    def __str__(self):
        resultat = '\nGramàtica:\n'
        for cap, cos in self.dicc.items():
            if cos:
                resultat += f'{cap} → '
                produccions = [' '.join(produccio) for produccio in cos]
                resultat += ' | '.join(produccions)
                resultat += '\n'
        return resultat
    