class Nodo:
    def __init__(self,info):
        self.info = info
        self.esq = None
        self.dir = None
class ArvBin:
    def __init__(self,raiz):
        self.raiz = Nodo(raiz)
        self.NumeroDeNodos = 0
    def vazia(self):
        if self.NumeroDeNodos == 0:
            return(True)
        return(False)
    def buscar(self,info,raiz):
        if raiz != None:
            if raiz.info == info:
                return(raiz)
            else:
                aux = self.buscar(info,raiz.esq)
                if aux != False:
                    return(aux)
                else:
                    return(self.buscar(info,raiz.dir))
        return(False)
    def inserirEsquerda(self,infoPai,infoFilho): 
        pai = self.buscar(infoPai,self.raiz)
        if pai != False and pai.esq == None:
            pai.esq = Nodo(infoFilho)
            self.NumeroDeNodos += 1
            return(True)
        return(False)
    def inserirDireita(self,infoPai,infoFilho):
        pai = self.buscar(infoPai,self.raiz)
        if pai != False and pai.dir == None:
            pai.dir = Nodo(infoFilho)
            self.NumeroDeNodos += 1
            return(True)
        return(False)
    def buscarPai(self,info,raiz):
        if raiz != None:
            if raiz.esq != None:
                if raiz.esq.info == info:
                    return(raiz)
            if raiz.dir != None:
                if raiz.dir.info == info:
                    return(raiz)
            aux = self.buscarPai(info,raiz.esq)
            if aux != False:
                return(aux)
            else:
                return(self.buscarPai(info,raiz.dir))
        return(False)
    def remover(self,info):
        if self.raiz.info == info:
            aux = self.raiz
            if aux.esq == None and aux.dir == None:
                self.raiz = None
                self.NumeroDeNodos = 0
                return(True)
        else:
            pai = self.buscarPai(info,self.raiz)
            if pai != False:
                if pai.esq.info == info:
                    filho = pai.esq
                    if filho.esq == None and filho.dir == None:
                        pai.esq = None
                        return(True)
                else:
                    filho = pai.dir
                    if filho.esq == None and filho.dir == None:
                        pai.dir = None
                        return(True)
        return(False)
    def printarPre(self,raiz):
        if raiz != None:
            print(raiz.info)
            self.printarPre(raiz.esq)
            self.printarPre(raiz.dir)
            return(True)
        return(False)
    def printarCentral(self,raiz):
        if raiz != None:
            self.printarCentral(raiz.esq)
            print(raiz.info)
            self.printarCentral(raiz.dir)
            return(True)
        return(False)
    def printarPos(self,raiz):
        if raiz != None:
            self.printarPos(raiz.esq)
            self.printarPos(raiz.dir)
            print(raiz.info)
            return(True)
        return(False)