from src.modelo.erro_semantico import ErroSemantico
from src.modelo.pilha import Pilha
from src.modelo.linguagem_mgol import GRAMATICA_LIVRE_CONTEXTO
from src.modelo.token import Token


class AnalisadorSemantico:
    def __init__(self, tabela_simbolos):
        self._tabela_simbolos = tabela_simbolos
        self._pilha_semantica = Pilha()
        self._linha = 1
        self._coluna = 0
        self._variaveis_temporarias = []
        self.erros = []
        self.codigo = ''

    def empilhar(self, a):
        self._pilha_semantica.empilhar(Token(a.classe.lower(), a.lexema, a.tipo))

    def analyze(self, numero_regra, linha, coluna):
        self._linha = linha
        self._coluna = coluna

        esquerda, direita = GRAMATICA_LIVRE_CONTEXTO[numero_regra]
        desempilhados = self._pilha_semantica.desempilhar(len(direita))

        if numero_regra == 1:
            self._pilha_semantica.empilhar(self.regras1(esquerda, direita, desempilhados))
            return
        elif numero_regra == 2:
            self._pilha_semantica.empilhar(self.regras2(esquerda, direita, desempilhados))
            return
        elif numero_regra == 3:
            self._pilha_semantica.empilhar(self.regras3(esquerda, direita, desempilhados))
            return
        elif numero_regra == 4:
            self._pilha_semantica.empilhar(self.regras4(esquerda, direita, desempilhados))
            return
        elif numero_regra == 5:
            self._pilha_semantica.empilhar(self.regras5(esquerda, direita, desempilhados))
            return
        elif numero_regra == 6:
            self._pilha_semantica.empilhar(self.regras6(esquerda, direita, desempilhados))
            return
        elif numero_regra == 7:
            self._pilha_semantica.empilhar(self.regras7(esquerda, direita, desempilhados))
            return
        elif numero_regra == 8:
            self._pilha_semantica.empilhar(self.regras8(esquerda, direita, desempilhados))
            return
        elif numero_regra == 9:
            self._pilha_semantica.empilhar(self.regras9(esquerda, direita, desempilhados))
            return
        elif numero_regra == 10:
            self._pilha_semantica.empilhar(self.regras10(esquerda, direita, desempilhados))
            return
        elif numero_regra == 11:
            self._pilha_semantica.empilhar(self.regras11(esquerda, direita, desempilhados))
            return
        elif numero_regra == 12:
            self._pilha_semantica.empilhar(self.regras12(esquerda, direita, desempilhados))
            return
        elif numero_regra == 13:
            self._pilha_semantica.empilhar(self.regras13(esquerda, direita, desempilhados))
            return
        elif numero_regra == 14:
            self._pilha_semantica.empilhar(self.regras14(esquerda, direita, desempilhados))
            return
        elif numero_regra == 15:
            self._pilha_semantica.empilhar(self.regras15(esquerda, direita, desempilhados))
            return
        elif numero_regra == 16:
            self._pilha_semantica.empilhar(self.regras16(esquerda, direita, desempilhados))
            return
        elif numero_regra == 17:
            self._pilha_semantica.empilhar(self.regras17(esquerda, direita, desempilhados))
            return
        elif numero_regra == 18:
            self._pilha_semantica.empilhar(self.regras18(esquerda, direita, desempilhados))
            return
        elif numero_regra == 19:
            self._pilha_semantica.empilhar(self.regras19(esquerda, direita, desempilhados))
            return
        elif numero_regra == 20:
            self._pilha_semantica.empilhar(self.regras20(esquerda, direita, desempilhados))
            return
        elif numero_regra == 21:
            self._pilha_semantica.empilhar(self.regras21(esquerda, direita, desempilhados))
            return
        elif numero_regra == 22:
            self._pilha_semantica.empilhar(self.regras22(esquerda, direita, desempilhados))
            return
        elif numero_regra == 23:
            self._pilha_semantica.empilhar(self.regras23(esquerda, direita, desempilhados))
            return
        elif numero_regra == 24:
            self._pilha_semantica.empilhar(self.regras24(esquerda, direita, desempilhados))
            return
        elif numero_regra == 25:
            self._pilha_semantica.empilhar(self.regras25(esquerda, direita, desempilhados))
            return
        elif numero_regra == 26:
            self._pilha_semantica.empilhar(self.regras26(esquerda, direita, desempilhados))
            return
        elif numero_regra == 27:
            self._pilha_semantica.empilhar(self.regras27(esquerda, direita, desempilhados))
            return
        elif numero_regra == 28:
            self._pilha_semantica.empilhar(self.regras28(esquerda, direita, desempilhados))
            return
        elif numero_regra == 29:
            self._pilha_semantica.empilhar(self.regras29(esquerda, direita, desempilhados))
            return
        elif numero_regra == 30:
            self._pilha_semantica.empilhar(self.regras30(esquerda, direita, desempilhados))
            return
        elif numero_regra == 31:
            self._pilha_semantica.empilhar(self.regras31(esquerda, direita, desempilhados))
            return
        elif numero_regra == 32:
            self._pilha_semantica.empilhar(self.regras32(esquerda, direita, desempilhados))
            return

    def regras1(self, esquerda, direita, desempilhados):  # P' -> P
        return Token(esquerda, None, None)

    def regras2(self, esquerda, direita, desempilhados):  # P -> inicio V A
        return Token(esquerda, None, None)

    def regras3(self, esquerda, direita, desempilhados):  # V -> varinicio LV
        return Token(esquerda, None, None)

    def regras4(self, esquerda, direita, desempilhados):  # LV -> D LV
        return Token(esquerda, None, None)

    def regras5(self, esquerda, direita, desempilhados):  # LV -> varfim pt_v
        # self.codigo += '\n\n\n'
        return Token(esquerda, None, None)

    def regras6(self, esquerda, direita, desempilhados):  # D -> TIPO L pt_v
        TIPO = desempilhados[2]
        L = desempilhados[1]
        pt_v = desempilhados[0]

        L.tipo = TIPO.tipo  # ??

        for id in L.lexema.split(','):
            self.codigo += f'{TIPO.tipo} {id}{pt_v.lexema}\n'

        return Token(esquerda, None, TIPO.tipo)

    def regras7(self, esquerda, direita, desempilhados):  # L -> id vir L
        id = desempilhados[2]
        vir = desempilhados[1]
        L = desempilhados[0]

        TIPO = self._pilha_semantica.obterPrimeiro('TIPO')

        simbolo = self._tabela_simbolos.buscar(id.lexema)
        simbolo.tipo = TIPO.tipo

        return Token(esquerda, f'{id.lexema},{L.lexema}', TIPO.tipo)

    def regras8(self, esquerda, direita, desempilhados):  # L -> id
        id = desempilhados[0]

        TIPO = self._pilha_semantica.obterPrimeiro('TIPO')

        simbolo = self._tabela_simbolos.buscar(id.lexema)
        simbolo.tipo = TIPO.tipo

        # self.codigo += f'{id.lexema}'
        return Token(esquerda, id.lexema, TIPO.tipo)

    def regras9(self, esquerda, direita, desempilhados):  # TIPO -> inteiro
        inteiro = desempilhados[0]
        return Token(esquerda, inteiro.lexema, inteiro.tipo)

    def regras10(self, esquerda, direita, desempilhados):  # TIPO -> real
        real = desempilhados[0]
        return Token(esquerda, real.lexema, real.tipo)

    def regras11(self, esquerda, direita, desempilhados):  # TIPO -> literal
        literal = desempilhados[0]
        return Token(esquerda, literal.lexema, literal.tipo)

    def regras12(self, esquerda, direita, desempilhados):  # A -> ES A
        return Token(esquerda, None, None)

    def regras13(self, esquerda, direita, desempilhados):  # ES -> leia id pt_v
        id = desempilhados[1]

        simbolo = self._tabela_simbolos.buscar(id.lexema)

        if simbolo is not None and simbolo.tipo is not None:
            if simbolo.tipo == 'literal':
                self.codigo += f'scanf("%s", {id.lexema});\n'
            if simbolo.tipo == 'inteiro':
                self.codigo += f'scanf("%d", &{id.lexema});\n'
            if simbolo.tipo == 'real':
                self.codigo += f'scanf("%f", &{id.lexema});\n'
        else:
            erro_semantico = ErroSemantico('Erro: Variável {} não declarada (linha {}, coluna {}).'
                                           .format(repr(id.lexema), repr(self._linha), repr(self._coluna)))

            self.tratarErroSemantico(erro_semantico)

        return Token(esquerda, None, None)

    def regras14(self, esquerda, direita, desempilhados):  # ES -> escreva ARG pt_v
        ARG = desempilhados[1]
        self.codigo += f'printf({ARG.lexema});\n'
        return Token(esquerda, None, None)

    def regras15(self, esquerda, direita, desempilhados):  # ARG -> lit
        lit = desempilhados[0]
        return Token(esquerda, lit.lexema, lit.tipo)

    def regras16(self, esquerda, direita, desempilhados):  # ARG -> num
        num = desempilhados[0]
        return Token(esquerda, num.lexema, num.tipo)

    def regras17(self, esquerda, direita, desempilhados):  # ARG -> id
        id = desempilhados[0]

        simbolo = self._tabela_simbolos.buscar(id.lexema)

        ARG = Token(esquerda, id.lexema, id.tipo)

        if simbolo is not None and simbolo.tipo is not None:
            ARG = Token(esquerda, simbolo.lexema, simbolo.tipo)
        else:
            erro_semantico = ErroSemantico('Erro semântico - Variável {} não declarada (linha {}, coluna {}).'
                                           .format(repr(id.lexema), repr(self._linha), repr(self._coluna)))

            self.tratarErroSemantico(erro_semantico)

        return ARG

    def regras18(self, esquerda, direita, desempilhados):  # A -> CMD A
        return Token(esquerda, None, None)

    def regras19(self, esquerda, direita, desempilhados):  # CMD -> id atr LD pt_v
        id = desempilhados[3]
        LD = desempilhados[1]

        simbolo = self._tabela_simbolos.buscar(id.lexema)
        if simbolo is not None and simbolo.tipo is not None:
            if LD.tipo == simbolo.tipo:
                self.codigo += f'{id.lexema}={LD.lexema};\n'
            else:
                erro_semantico = ErroSemantico(
                    'Erro semântico - Tipos diferentes para atribuição (linha {}, coluna {}).'
                    .format(repr(self._linha), repr(self._coluna)))

                self.tratarErroSemantico(erro_semantico)
        else:
            erro_semantico = ErroSemantico('Erro semântico - Variável {} não declarada (linha {}, coluna {}).'
                                           .format(repr(id.lexema), repr(self._linha), repr(self._coluna)))

            self.tratarErroSemantico(erro_semantico)

        return Token(esquerda, None, None)

    def regras20(self, esquerda, direita, desempilhados):  # LD -> OPRD opa OPRD
        OPRD = desempilhados[2]
        opa = desempilhados[1]
        OPRD1 = desempilhados[0]

        LD = Token(esquerda, None, None)

        if OPRD.tipo != 'literal' and OPRD1.tipo == OPRD.tipo:
            LD.tipo = OPRD.tipo

            variavel_temporaria = len(self._variaveis_temporarias)
            self.codigo += f'T{variavel_temporaria}={OPRD.lexema}{opa.lexema}{OPRD1.lexema};\n'
            self._variaveis_temporarias.append(LD.tipo)

            LD.lexema = f'T{variavel_temporaria}'

        else:
            erro_semantico = ErroSemantico('Erro semântico - Operandos com tipos incompatíveis (linha {}, coluna {}).'
                                           .format(repr(self._linha), repr(self._coluna)))

            self.tratarErroSemantico(erro_semantico)

        return LD

    def regras21(self, esquerda, direita, desempilhados):  # LD -> OPRD
        OPRD = desempilhados[0]
        return Token(esquerda, OPRD.lexema, OPRD.tipo)

    def regras22(self, esquerda, direita, desempilhados):  # OPRD -> id
        id = desempilhados[0]

        simbolo = self._tabela_simbolos.buscar(id.lexema)

        OPRD = Token(esquerda, id.lexema, None)
        if simbolo is not None and simbolo.tipo is not None:
            OPRD.tipo = simbolo.tipo
        else:
            erro_semantico = ErroSemantico('Erro semântico - Variável {} não declarada (linha {}, coluna {}).'
                                           .format(repr(id.lexema), repr(self._linha), repr(self._coluna)))

            self.tratarErroSemantico(erro_semantico)

        return OPRD

    def regras23(self, esquerda, direita, desempilhados):  # OPRD -> num
        num = desempilhados[0]
        return Token(esquerda, num.lexema, num.tipo)

    def regras24(self, esquerda, direita, desempilhados):  # A -> COND A
        return Token(esquerda, None, None)

    def regras25(self, esquerda, direita, desempilhados):  # COND -> CAB CP
        self.codigo += '}\n'
        return Token(esquerda, None, None)

    def regras26(self, esquerda, direita, desempilhados):  # CAB -> se ab_p EXP_R fc_p entao
        EXP_R = desempilhados[2]
        self.codigo += f'if({EXP_R.lexema})''\n{\n'
        return Token(esquerda, None, None)

    def regras27(self, esquerda, direita, desempilhados):  # EXP_R -> OPRD opr OPRD
        OPRD = desempilhados[2]
        opr = desempilhados[1]
        OPRD1 = desempilhados[0]

        variavel_temporaria = len(self._variaveis_temporarias)
        self.codigo += f'T{variavel_temporaria}={OPRD.lexema}{opr.lexema}{OPRD1.lexema};\n'
        self._variaveis_temporarias.append('inteiro')

        return Token(esquerda, f'T{variavel_temporaria}', None)

    def regras28(self, esquerda, direita, desempilhados):  # CP -> ES CP
        return Token(esquerda, None, None)

    def regras29(self, esquerda, direita, desempilhados):  # CP -> CMD CP
        return Token(esquerda, None, None)

    def regras30(self, esquerda, direita, desempilhados):  # CP -> COND CP
        return Token(esquerda, None, None)

    def regras31(self, esquerda, direita, desempilhados):  # CP -> fimse
        return Token(esquerda, None, None)

    def regras32(self, esquerda, direita, desempilhados):  # A -> fim
        return Token(esquerda, None, None)

    def tratarErroSemantico(self, erro_semantico):
        print(erro_semantico)
        self.erros.append(erro_semantico)

    def _gerarVariaveisTemporarias(self):
        variaveis_temporarias = ''
        variaveis_temporarias += '/*-------Variáveis temporárias----------*/\n'
        for i, T in enumerate(self._variaveis_temporarias):
            variaveis_temporarias += f'{T} T{i};\n'
        variaveis_temporarias += '/*--------------------------------------*/\n'

        return variaveis_temporarias

    def gerar(self, arquivo_objetivo):
        inicio = '#include <stdio.h>\ntypedef char literal[256];\nvoid main(void)\n{\n'
        variaveis_temporarias = self._gerarVariaveisTemporarias()

        codigo_final = inicio + variaveis_temporarias + self.codigo + '}'

        codigo_final = codigo_final.replace('inteiro', 'int')
        codigo_final = codigo_final.replace('real', 'double')

        #print(codigo_final)

        arquivo_objetivo.write(codigo_final)



