from src.modelo.token import Token

class AutomatoFinitoDeterministico:
    def __init__(self, estados, simbolos, estado_inicial, estados_finais, transicoes):
        self._estados = estados
        self._simbolos = simbolos
        self._estado_inicial = estado_inicial
        self._estados_finais = estados_finais
        self._transicoes = transicoes

        self._estado = self._estado_inicial
        self._lexema = ''

    def leia(self, caractere) -> Token:

        if not self._simbolos.__contains__(caractere):
            token = Token('ERRO', caractere, None)
            self._estado = self._estado_inicial
            self._lexema = ''
            return token

        if self._estado is None or self._transicoes[self._estado].get(caractere) is None:
            token = self.finaliza()
        else:
            token = None

        self.transiciona(caractere)
        return token

    def finaliza(self) -> Token:
        if self._estado in self._estados_finais:
            token = self._estados_finais[self._estado]
            token.lexema = self._lexema

            self._estado = self._estado_inicial
            self._lexema = ''

            return token
        else:
            token = Token('ERRO', self._lexema, None)
            self._estado = self._estado_inicial
            self._lexema = ''
            return token

    def transiciona(self, caractere):
        self._lexema += caractere
        self._estado = self._transicoes[self._estado].get(caractere)
