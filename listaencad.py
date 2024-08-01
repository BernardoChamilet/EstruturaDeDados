class Nodo:
	def __init__(self,info):
		self.info = info
		self.prox = None

class ListaEnc:
	def __init__(self):
		self.inicio = None
		self.tam = 0
	def vazia(self):
		if self.tam == 0:
			return(True)
		return(False)
	def imprimir(self):
		aux = self.inicio
		if aux != None:
			while aux.prox != None:
				print(aux.info)
				aux = aux.prox
			print(aux.info)
		else:
			print(aux)
		return(True)
	def imprimirContrario(self):
		if self.tam != 0:
			printpos = self.tam
			while printpos > 0:
				aux = self.inicio
				pos = 1
				while pos < printpos:
					aux = aux.prox
					pos += 1
				print(aux.info)
				printpos -= 1
			return(True)
		return(False)
	def inserir(self,posicao,valor):
		if posicao > 0 and posicao <= self.tam + 1:
			x = Nodo(valor)
			if posicao == 1:
				x.prox = self.inicio
				self.inicio = x
				self.tam += 1
			else:
				aux = self.inicio
				cont = 1
				while cont < posicao - 1:
					if aux.prox != None: 
						aux = aux.prox
					cont += 1
				x.prox = aux.prox
				aux.prox = x
				self.tam += 1
			return(True)
		return(False)
	def buscar(self,valor):
		aux = self.inicio
		pos = 1
		while pos <= self.tam:
			if aux.info == valor:
				return(pos)
			pos += 1
			aux = aux.prox
		return(False)
	def consultar(self,pos):
		if pos > 0 and pos <= self.tam:
			aux = self.inicio
			cont = 1
			while cont <= pos:
				if cont == pos:
					return(aux.info)
				cont += 1
				aux = aux.prox
		return(False)
	def destruir(self):
		self.inicio = None
		self.tam = 0
		return(True)
	def remover(self,posicao):
		if posicao > 0 and posicao <= self.tam:
			aux = self.inicio
			if posicao == 1:
				self.inicio = aux.prox
			else:
				cont = 1
				while cont < posicao - 1:
					aux = aux.prox
					cont += 1
				aux.prox = aux.prox.prox
			self.tam -= 1
			return(True)
		return(False)
	def tamanho(self):
		return(self.tam)
	def comparar(self,lista):
		if self.tam != lista.tamanho():
			return(False)
		else:
			aux = self.inicio
			cont = 1
			while cont <= self.tam:
				if aux.info != lista.consultar(cont):
					return(False)
				aux = aux.prox
				cont += 1
			return(True)
"""		
lista = ListaEnc()
lista.inserir(1,3)
lista.inserir(1,1)
lista.inserir(2,2)
lista.inserir(4,4)
lista.remover(3)
lista2 = ListaEnc()
lista2.inserir(1,3)
lista2.inserir(1,10)
lista2.inserir(2,2)
lista2.inserir(4,4)
lista2.remover(3)
print(lista.comparar(lista2))
lista.imprimir()
lista.imprimirContrario()
print(lista.buscar(3))
print(lista.consultar(2))
lista.destruir()
lista.imprimir()
print(lista.tam)
"""