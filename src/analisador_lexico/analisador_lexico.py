from src.modelo.automato_finito_deterministico import AutomatoFinitoDeterministico
from src.modelo.erro_lexico import ErroLexico
from src.modelo.linguagem_mgol import ESTADOS, LETRAS, NUMEROS, SIMBOLOS, ESTADO_INICIAL, ESTADOS_FINAIS, TRANSICOES, PALAVRAS
from src.modelo.token import Token

class AnalisadorLexico:
    def __init__(self, arquivo_fonte, tabela_simbolos):
        self._arquivo_fonte = arquivo_fonte
        self._automato = AutomatoFinitoDeterministico(
            ESTADOS,
            LETRAS + NUMEROS + SIMBOLOS,
            ESTADO_INICIAL,
            ESTADOS_FINAIS,
            TRANSICOES
        )
        self._linha = 1
        self._coluna = 0
        self.erros = []

        self._tabela_simbolos = tabela_simbolos
        for palavra in PALAVRAS:
            self._tabela_simbolos.inserir(Token(palavra, palavra, palavra))

    def proximoToken(self) -> (Token, int, int):

        token = self._prosseguirLeitura()

        token = self._encontrarPalavraReservada(token)

        self._atualizarTabelaSimbolos(token)

        # print(token)

        return token, self._linha, self._coluna

    def _prosseguirLeitura(self) -> Token:
        while True:
            caractere = self._arquivo_fonte.read(1)

            token = self._automato.leia(caractere)

            self._atualizarDadosLeitura(caractere)

            if token is not None and token.classe == 'ERRO':
                self._tratarErroLexico(token)

            if token is not None and token.classe != 'Ignorar' and token.classe != 'Comentário' and token.classe != 'ERRO':
                break

        return token

    def _tratarErroLexico(self, token_erro):
        erro_lexico = ErroLexico('ERRO léxico – Caractere inválido na linguagem, linha {}, coluna {}: {}'
                                 .format(repr(self._linha), repr(self._coluna), repr(token_erro.lexema)))

        print(erro_lexico)
        self.erros.append(erro_lexico)

    def _encontrarPalavraReservada(self, token) -> Token:
        if token.classe == 'id' and token.lexema in PALAVRAS:
            return Token(token.lexema, token.lexema, token.lexema)

        return token

    def _atualizarTabelaSimbolos(self, token):
        if token.classe == 'id':
            self._tabela_simbolos.inserir(Token(token.classe, token.lexema, token.tipo))

    def _atualizarDadosLeitura(self, caractere):
        if caractere == '\n':
            self._linha += 1
            self._coluna = 0
        else:
            self._coluna += 1
