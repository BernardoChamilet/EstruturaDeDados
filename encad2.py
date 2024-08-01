class Nodo:
	def __init__(self,info):
		self.info = info
		self.prox = None
		self.ant = None

class ListaEnc:
	def __init__(self):
		self.inicio = None
		self.tam = 0
		self.fim = None
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
	def inserir(self,posicao,valor):
		if posicao > 0 and posicao <= self.tam + 1:
			x = Nodo(valor)
			if posicao == 1:
				x.prox = self.inicio
				if x.prox != None:
					x.prox.ant = x
				self.inicio = x
			else:
				aux = self.inicio
				cont = 1
				while cont < posicao - 1:
					if aux.prox != None: 
						aux = aux.prox
					cont += 1
				x.prox = aux.prox
				x.ant = aux
				aux.prox = x
				if x.prox != None:
					x.prox.ant = x
			if posicao == self.tam + 1:
				self.fim = x
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
		aux = self.inicio
		while aux.prox != None:
			aux.ant = None
			aux = aux.prox
		aux.ant = None
		aux = None
		self.inicio = None
		self.fim = None
		self.tam = 0
		return(True)
	def remover(self,posicao):
		if posicao > 0 and posicao <= self.tam:
			aux = self.inicio
			if posicao == 1:
				self.inicio = aux.prox
				if self.inicio != None:
					self.inicio.ant = None
			else:
				cont = 1
				while cont < posicao - 1:
					aux = aux.prox
					cont += 1
				aux.prox = aux.prox.prox
				if aux.prox != None:
					aux.prox.ant = aux
				else:
					self.fim = aux
			self.tam -= 1
			if self.tam == 0:
				self.fim = None
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

lista = ListaEnc()
lista.inserir(1,3)
lista.inserir(1,1)
lista.inserir(2,2)
lista.inserir(4,4)
#print(lista.fim.info)
lista.remover(4)
#print(lista.fim.info)
#lista.remover(2)
#lista.remover(1)
lista.destruir()
print(lista.tamanho())
print(lista.fim)
print(lista.inicio)
lista.imprimir()
