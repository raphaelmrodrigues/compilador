class ErroSemantico(Exception):
    def __init__(self, erro):
        self.mensagem = erro

    def __repr__(self):
        return '{}'.format(repr(self.mensagem))
