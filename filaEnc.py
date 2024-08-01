class Nodo:
    def __init__(self,info):
        self.info = info
        self.prox = None

class Fila:
    def __init__(self):
        self.ini = None
        self.fim = None
    def inserir(self,dado):
        aux = Nodo(dado)
        if self.ini == None:
            self.ini = aux
            self.fim = aux
        else:
            self.fim.prox = aux
            self.fim = aux
    def remover(self):
        if self.ini != None:
            self.ini = self.ini.prox
    def consultar(self):
        if self.ini != None:
            aux = self.ini.info
            return(aux)
    def destruir(self):
        while self.ini != None:
            self.remover()
        self.fim = None
    def vazia(self):
        if self.ini == None:
            return(True)
        else:
            return(False)