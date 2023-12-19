import os
import pandas as pd

from src.modelo.erro_sintatico import ErroSintatico
from src.modelo.pilha import Pilha
from src.modelo.linguagem_mgol import GRAMATICA_LIVRE_CONTEXTO


class AnalisadorSintatico:
    def __init__(self, scanner, generator):
        self._scanner = scanner
        self._generator = generator
        self._pilha_sintatica = Pilha(elemento_inicial=0)
        self._actionDict = self._csvToDict('arquivos/action.csv')
        self._gotoDict = self._csvToDict('arquivos/goto.csv')
        self.erros = []

    def parse(self):
        a, linha, coluna = self._scanner.proximoToken()
        while True:
            s = self._pilha_sintatica.topo()
            action = self._action(s, a)

            if action[0] == 'S':
                t = int(action[1:])
                self._pilha_sintatica.empilhar(t) # Pilha sintática
                self._generator.empilhar(a) # Pilha semântica
                a, linha, coluna = self._scanner.proximoToken()

            elif action[0] == 'R':
                numero_regra = int(action[1:]) + 1
                A, B = GRAMATICA_LIVRE_CONTEXTO[numero_regra]

                self._pilha_sintatica.desempilhar(len(B))
                t = self._pilha_sintatica.topo()

                goto = self._goto(t, A)
                self._pilha_sintatica.empilhar(goto)

                print(f'{A} -> {" ".join(B)}')
                self._generator.analyze(numero_regra, linha, coluna)

            elif action == 'ACC' or a.classe.lower() == 'eof':
                break

            else:
                a, linha, coluna = self._panic_mode_error_recovery(a, linha, coluna, action)

    def _panic_mode_error_recovery(self, token, linha, coluna, action):
        erro_sintatico = ErroSintatico('ERRO sintático - Expressão não reconhecida na linguagem, linha {}, coluna {}: {} ({})'
                                       .format(repr(linha), repr(coluna), repr(token.lexema), repr(action)))

        print(erro_sintatico)
        self.erros.append(erro_sintatico)

        while True:
            a, linha, coluna = self._scanner.proximoToken()

            if a.classe.lower() == 'pt_v' or a.classe.lower() == 'eof':
                break

        return a, linha, coluna

    def _action(self, s, a):
        return self._actionDict[s].get(a.classe.lower())

    def _goto(self, t, A):
        return int(self._gotoDict[t].get(A))

    def _csvToDict(self, path):
        result = pd.read_csv(os.path.join(os.path.dirname(__file__), path), sep=';', encoding="utf-8")
        result = result.set_index('estado')
        result = result.where(pd.notnull(result), None)
        result = result.T.to_dict()
        return result
