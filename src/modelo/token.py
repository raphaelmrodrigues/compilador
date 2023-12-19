class Token:
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __repr__(self):
        return 'Classe: {}, Lexema: {}, Tipo: {}'\
            .format(repr(self.classe), repr(self.lexema), repr(self.tipo))

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.classe == other.classe and self.lexema == other.lexema
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
