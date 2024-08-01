class Nodo:
    def __init__(self,chave,info):
        self.info = info
        self.chave = chave
        self.esq = None
        self.dir = None

class ABP:
    def __init__(self,chave,info):
        self.raiz = Nodo(chave,info)
    def localizar(self,chave):
        aux = self.raiz
        while aux != None:
            if aux.chave == chave:
                return(aux)
            else:
                if aux.chave > chave:
                    aux = aux.esq
                else:
                    aux = aux.dir
        return(None)
    def inserir(self,chave,info):
        aux = self.raiz
        while True:
            if aux.chave == chave:
                aux.info = info
                return(True)
            else:
                if aux.chave > chave:
                    if aux.esq == None:
                        novo = Nodo(chave,info)
                        aux.esq = novo
                        return(True)
                    else:
                        aux = aux.esq
                else:
                    if aux.dir == None:
                        novo = Nodo(chave,info)
                        aux.dir = novo
                        return(True)
                    else:
                        aux = aux.dir
    def eFolha(self,nodo):
        if nodo.esq == None and nodo.dir == None:
            return(True)
        return(False)
    def temDoisFilhos(self,nodo):
        if nodo.esq != None and nodo.dir != None:
            return(True)
        return(False)
    def buscarPai(self,chave,raiz):
        if raiz != None:
            if raiz.esq != None:
                if raiz.esq.chave == chave:
                    return(raiz)
            if raiz.dir != None:
                if raiz.dir.chave == chave:
                    return(raiz)
            aux = self.buscarPai(chave,raiz.esq)
            if aux != False:
                return(aux)
            else:
                return(self.buscarPai(chave,raiz.dir))
        return(False)
    def excluir(self,chave):
        excluido = self.localizar(chave)
        if excluido != None:
            #se é folha
            if self.eFolha(excluido):
                pai = self.buscarPai(chave,self.raiz)
                if pai != False:
                    if pai.esq.chave == chave:
                        pai.esq = None
                        return(True)
                    else:
                        pai.dir = None
                        return(True)
            else:
                #se tem dois filhos
                if self.temDoisFilhos(excluido):
                    aux = excluido
                    aux = aux.esq
                    alturaEsq = 1
                    while aux != None:
                        aux = aux.dir
                        alturaEsq += 1
                    aux = excluido
                    aux = aux.dir
                    alturaDir = 1
                    while aux != None:
                        aux = aux.esq
                        alturaDir += 1
                    #se excluir na arvore da esquerda for melhor p balancear
                    if alturaEsq >= alturaDir:
                        aux = excluido
                        aux = aux.esq
                        while True:
                            if aux.dir == None:
                                excluido.info = aux.info
                                excluido.chave = aux.chave
                                aux.chave = "exclui"
                                #se o nodo substituido for folha
                                if self.eFolha(aux):
                                    pai = self.buscarPai("exclui",self.raiz)
                                    if pai != False:
                                        if pai.esq.chave == "exclui":
                                            pai.esq = None
                                            return(True)
                                        else:
                                            pai.dir = None
                                            return(True)
                                else:
                                    #se o nodo substituido tiver um filho(na esquerda necessariamente)
                                    pai = self.buscarPai("exclui",self.raiz)
                                    filho = aux.esq
                                    if pai != False:
                                        if pai.esq.chave == "exclui":
                                            pai.esq = filho
                                            return(True)
                                        else:
                                            pai.dir = filho
                                            return(True)
                            aux = aux.dir
                    #se excluir na arvore da direita for melhor pra balancear
                    else:
                        aux = excluido
                        aux = aux.dir
                        while True:
                            if aux.esq == None:
                                excluido.info = aux.info
                                excluido.chave = aux.chave
                                aux.chave = "exclui"
                                #se o nodo substituido for folha
                                if self.eFolha(aux):
                                    pai = self.buscarPai("exclui",self.raiz)
                                    if pai != False:
                                        if pai.esq.chave == "exclui":
                                            pai.esq = None
                                            return(True)
                                        else:
                                            pai.dir = None
                                            return(True)
                                else:
                                    #se o nodo substituido tiver um filho(na direita necessariamente)
                                    pai = self.buscarPai("exclui",self.raiz)
                                    filho = aux.dir
                                    if pai != False:
                                        if pai.esq.chave == "exclui":
                                            pai.esq = filho
                                            return(True)
                                        else:
                                            pai.dir = filho
                                            return(True)
                            aux = aux.esq
                else:
                    #se tem um filho
                    if excluido.dir == None:
                        filho = excluido.esq
                    else:
                        filho = excluido.dir
                    pai = self.buscarPai(chave,self.raiz)
                    if pai != False:
                        if pai.esq.chave == chave:
                            pai.esq = filho
                            return(True)
                        else:
                            pai.dir = filho
                            return(True)
        return(False)
    def printarCentralEsq(self,raiz):
        if raiz != None:
            self.printarCentralEsq(raiz.esq)
            print(raiz.info)
            self.printarCentralEsq(raiz.dir)
            return(True)
        return(False)