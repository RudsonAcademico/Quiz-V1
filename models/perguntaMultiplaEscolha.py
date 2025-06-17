from models.pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, opcoes, resposta_correta):
        super().__init__(texto, resposta_correta)
        self._opcoes = opcoes

    def exibir(self):
        return self._texto, self._opcoes

    def verificar_resposta(self, resposta_usuario):
        try:
            return self._opcoes[int(resposta_usuario)-1] == self._resposta_correta
        except:
            return False