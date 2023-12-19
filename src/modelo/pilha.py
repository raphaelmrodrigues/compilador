class Pilha:
    def __init__(self, elemento_inicial=None):
        if elemento_inicial is not None:
            self._pilha = [elemento_inicial]
        else:
            self._pilha = []

    def topo(self):
        return self._pilha[-1]

    def empilhar(self, elemento):
        self._pilha.append(elemento)

    def desempilhar(self, numero_elementos):
        desempilhados = []
        for _ in range(numero_elementos):
            desempilhados.append(self._pilha.pop())
        return desempilhados

    def get(self):
        return self._pilha

    def obterPrimeiro(self, search):
        for elemento in reversed(self._pilha):
            if elemento.classe == search:
                return elemento
