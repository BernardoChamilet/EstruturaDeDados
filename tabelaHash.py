from listaencad import *

class Tabela:
    def __init__(self,max,primo):
        self.linhas = [ListaEnc()]*(max+1)
        self.primo = primo
    def h(self,n):
        pos = n % self.primo + 1
        return(pos)
    def buscar(self,chave):
        pos = self.h(chave)
        linha = self.linhas[pos]
        if linha.vazia():
            return(0)
        cont = 1
        tam = linha.tamanho()
        while cont <= tam:
            if chave == linha.consultar(cont)[0]:
                return(pos,cont)
            cont += 1
        return(0)      
    def inserir(self,chave,valor):
        pos = self.buscar(chave)
        if pos == 0:
            posTab = self.h(chave)
            linha = self.linhas[posTab]
            linha.inserir(1,[chave,valor])
            return(True) 
        posTab = pos[0]
        posEncad = pos[1]
        linha = self.linhas[posTab]
        linha.consultar(posEncad)[1] = valor
        #linha.remover(posEncad)
        #linha.inserir(posEncad,[chave,valor])
    def consultar(self,chave):
        pos = self.buscar(chave)
        if pos == 0:
            return(False)
        posTab = pos[0]
        posEncad = pos[1]
        linha = self.linhas[posTab]
        valor = linha.consultar(posEncad)
        return(valor[1])
    def excluir(self,chave):
        pos = self.buscar(chave)
        if pos == 0:
            return(False)
        posTab = pos[0]
        posEncad = pos[1]
        linha = self.linhas[posTab]
        linha.remover(posEncad)
        return(True)
    def destruir(self):
        self.linhas = [ListaEnc()]*(max+1)

def proxPrimo(n,listaPrimos):
    if n in listaPrimos:
        return(n)
    else:
        cont = 0
        x = len(listaPrimos)
        while cont < x:
            if listaPrimos[cont] > n:
                return(listaPrimos[cont])
            cont += 1
            
listaPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
tabela = Tabela(10,proxPrimo(10,listaPrimos))
print(tabela.buscar(1))
tabela.inserir(42,"oi")
tabela.inserir(42,"ola")
print(tabela.buscar(42))
print(tabela.consultar(42))
tabela.inserir(31,"tchau")
print(tabela.buscar(31))
print(tabela.consultar(31))
print(tabela.buscar(42))
print(tabela.consultar(42))
tabela.excluir(31)
print(tabela.buscar(31))
print(tabela.consultar(31))
print(tabela.buscar(42))
print(tabela.consultar(42))