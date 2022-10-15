import numpy as np



class vetorNaoOrdenado:

    def __init__(self, capacidade):

        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):

        if self.ultima_posicao == -1:
            print('O vetor esta vazio')

        else:
            for i in range(self.ultima_posicao + 1):
                 print(i, '-' , self.valores[i])


    def insere(self, valor):

        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida')

        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor


    def pesquisar(self, valor):

        for i in range(self.ultima_posicao + 1):

            if valor == self.valores[i]:
                return i

        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1
vetor = vetorNaoOrdenado(10)

vetor.insere(15)
vetor.insere(6)
vetor.insere(3)
vetor.insere(7)

vetor.excluir(3)
vetor.imprime()

print(vetor.pesquisar(15))
