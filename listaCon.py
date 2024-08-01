class Lista:
	def __init__(self, max):
		self.max = max
		self.vetor = [None] * self.max
		self.ini = -1
		self.fim = -1
	def vazia(self):
		if (self.ini == -1) and (self.fim == -1):
			return(True)
		else:
			return(False)
	def tamanho(self):
		if self.vazia():
			return(0)
		tamanho = self.fim - self.ini + 1
		return(tamanho)
	def inserir(self, posicao, dado):
		if (self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.tamanho()+1:
			if self.vazia():
				self.ini = self.max // 2
				self.fim = self.max // 2
			elif (self.fim != self.max - 1):
				for i in range(self.fim, self.ini + posicao -2, -1):
					self.vetor[i+1] = self.vetor[i]
				self.fim = self.fim + 1
			else:
				for i in range(self.ini, self.ini + posicao - 1):
					self.vetor[i-1] = self.vetor[i]
				self.ini = self.ini - 1
			self.vetor[self.ini + posicao - 1] = dado
			return(True)
		else:
			return(False)
	def remover(self,posicao):
		if posicao > self.tamanho():
			return(False)
		cont = self.ini + posicao - 1
		while cont < self.fim:
			self.vetor[cont] = self.vetor[cont+1]
			cont += 1
		self.fim = self.fim - 1
		return(True)
	def limpar(self):
		if not self.vazia():
			cont = self.ini
			while cont <= self.fim:
				self.vetor[cont] = None
				cont += 1
			self.ini = -1
			self.fim = -1
		return(True)
	def imprimir(self):
		if not self.vazia():
			cont = self.ini
			while cont <= self.fim:
				print(self.vetor[cont])
				cont += 1
		return(True)
	def localizar(self,dado):
		if not self.vazia():
			cont = self.ini
			while cont <= self.fim:
				if dado == self.vetor[cont]:
					return(cont - self.ini + 1)
				cont += 1
