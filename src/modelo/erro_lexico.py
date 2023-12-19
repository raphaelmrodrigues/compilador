class ErroLexico(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __repr__(self):
        return '{}'.format(repr(self.mensagem))
