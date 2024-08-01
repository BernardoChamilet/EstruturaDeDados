from filaEnc import *
from pilhaEnc import *

def ordena(fila):
    pilha1 = pilhaEnc()
    pilha2 = pilhaEnc()
    pilha1.empilhar(fila.consultar())
    fila.remover()
    while fila.vazia() != True:
        if pilha1.consultar() > fila.consultar() or pilha1.consultar() == False:
            pilha1.empilhar(fila.consultar())
            fila.remover()
            while pilha2.consultar() != False:
                pilha1.empilhar(pilha2.consultar())
                pilha2.remover()
        else:
            pilha2.empilhar(pilha1.consultar())
            pilha1.remover()
    while pilha1.consultar() != False:
        fila.inserir(pilha1.consultar())
        pilha1.remover()
    return(fila)

#Testando TAD fila
fila = Fila()
fila.remover()
fila.inserir(5)
print(fila.consultar())
fila.inserir(4)
print(fila.consultar())
fila.remover()
print(fila.consultar())
fila.remover()
fila.inserir(3)
print(fila.consultar())
fila.inserir(8)
fila.destruir()
fila.inserir(2)
fila.inserir(1)
fila.inserir(5)
fila.inserir(3)
fila.inserir(4)
print(fila.consultar())
print("---------------")
#Testando ordenação
fila = ordena(fila)
print(fila.consultar())
fila.remover()
print(fila.consultar())
fila.remover()
print(fila.consultar())
fila.remover()
print(fila.consultar())
fila.remover()
print(fila.consultar())
fila.remover()