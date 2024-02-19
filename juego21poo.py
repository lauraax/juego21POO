class Carta:
    def __init__(self, valor, pinta):
        self.valor= valor
        self.pinta= pinta
    
    def dar_valor(self):
        if self.valor in ['J','Q','K']:
            return 10
        if self.valor =='A':
            return 1
        return int(self.valor)
    def mostrar(self):
        return self.valor + " de " + self.pinta
class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas=[]
        else:
            self.cartas=[Carta(u,p) 
                         for u in ['A','J','Q','K']+[str(x) for x in range(2,11)] 
                         for p in ['picas', 'treboles','corazones','diamantes']]

    def dar_valor(self):
        valor = 0
        for c in self.cartas:
            valor += c.dar_valor()
        return valor

if __name__=='__main__':
    m= Mazo(True)
    for c in m.cartas:
        print(c.mostrar())
    print (m.dar_valor())