class TabelaSimbolos:
    def __init__(self):
        self._simbolos = []

    def get(self):
        return self._simbolos

    def inserir(self, item):
        if item not in self._simbolos:
            self._simbolos.append(item)

    def buscar(self, lexema):
        for item in self._simbolos:
            if item.lexema == lexema:
                return item

        return None
