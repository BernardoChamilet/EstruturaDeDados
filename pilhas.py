from pilhaCont import *
from pilhaEnc import *

def comparar(pilha1,pilha2):
    while True:
        if pilha1.consultar() != pilha2.consultar():
            return(False)
        if pilha1.consultar() == pilha2.consultar() and pilha1.consultar() == False:
            return(True)
        pilha1.remover()
        pilha2.remover()


pilha1 = pilhaCont(4)
pilha1.remover()
print(pilha1.consultar())
pilha1.empilhar(1)
print(pilha1.consultar())
pilha1.empilhar(2)
print(pilha1.consultar())
pilha1.empilhar(3)
print(pilha1.consultar())
pilha1.empilhar(4)
print(pilha1.consultar())
pilha1.remover()
print(pilha1.consultar())
#pilha1.empilhar(5)
#print(pilha1.consultar())
#pilha1.destruir()
#print(pilha1.consultar())

pilha2 = pilhaEnc()
pilha2.remover()
print(pilha2.consultar())
pilha2.empilhar(1)
print(pilha2.consultar())
pilha2.empilhar(2)
print(pilha2.consultar())
pilha2.empilhar(3)
print(pilha2.consultar())
pilha2.empilhar(4)
print(pilha2.consultar())
pilha2.remover()
print(pilha2.consultar())
pilha2.empilhar(5)
print(pilha2.consultar())
#pilha2.destruir()
#print(pilha2.consultar())

print(comparar(pilha1,pilha2))
print(pilha1.consultar())
print(pilha2.consultar())