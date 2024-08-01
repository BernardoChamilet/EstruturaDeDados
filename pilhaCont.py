class pilhaCont:
    def __init__(self,tamanho):
        self.limite = tamanho - 1
        self.vetor = [None]*tamanho
        self.base = 0
        self.topo = self.base - 1
    def empilhar(self,dado):
        if self.topo != self.limite:
            self.topo += 1
            self.vetor[self.topo] = dado
            return(True)
        return(False)
    def remover(self):
        if self.topo >= self.base:
            self.topo -= 1
            return(True)
        return(False)
    def consultar(self):
        if self.topo >= self.base:
            return(self.vetor[self.topo])
        return(False)
    def destruir(self):
        self.topo = self.base-1
        return(True)