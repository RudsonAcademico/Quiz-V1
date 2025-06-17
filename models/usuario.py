class Usuario:
    def __init__(self, nome):
        self._nome = nome
        self._pontuacao = 0

    def adicionar_ponto(self):
        self._pontuacao += 1

    def get_pontuacao(self):
        return self._pontuacao

    def get_nome(self):
        return self._nome