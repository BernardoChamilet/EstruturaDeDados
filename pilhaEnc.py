class Nodo:
    def __init__(self,info):
        self.info = info
        self.prox = None
class pilhaEnc:
    def __init__(self):
        self.topo = None
    def empilhar(self,dado):
        nodo = Nodo(dado)
        if self.topo != None:
            nodo.prox = self.topo 
        self.topo = nodo
        return(True)
    def remover(self):
        if self.topo != None:
            self.topo = self.topo.prox
            return(True)
        return(False)
    def consultar(self):
        if self.topo != None:
            return(self.topo.info)
        return(False)
    def destruir(self):
        self.topo = None