import os

from src.analisador_lexico.analisador_lexico import AnalisadorLexico
from src.analisador_semantico.analisador_semantico import AnalisadorSemantico
from src.analisador_sintatico.analisador_sintatico import AnalisadorSintatico
from src.modelo.tabela_simbolos import TabelaSimbolos


def principal():
    tabela_simbolos = TabelaSimbolos()

    path_arquivo_fonte = os.path.join(os.path.dirname(__file__), '../FONTE.ALG')
    arquivo_fonte = open(path_arquivo_fonte, mode='r', encoding='utf-8')

    scanner = AnalisadorLexico(arquivo_fonte, tabela_simbolos)
    generator = AnalisadorSemantico(tabela_simbolos)
    parser = AnalisadorSintatico(scanner, generator)

    parser.parse()

    arquivo_fonte.close()

    path_arquivo_objetivo = os.path.join(os.path.dirname(__file__), '../PROGRAMA.c')
    arquivo_objetivo = open(path_arquivo_objetivo, mode='w', encoding='utf-8')

    if scanner.erros.__len__() == 0 and parser.erros.__len__() == 0 and generator.erros.__len__() == 0:
        generator.gerar(arquivo_objetivo)

    arquivo_objetivo.close()

    # print('\n============================== Símbolos =================================\n')
    # for simbolo in tabela_simbolos.get():
    #     print(simbolo)


principal()
