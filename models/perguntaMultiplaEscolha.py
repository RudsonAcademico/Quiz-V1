from models.pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, opcoes, resposta_correta):
        super().__init__(texto, resposta_correta)
        self._opcoes = opcoes

    def exibir(self):
        print(f"\n{self._texto}")
        for i, opcao in enumerate(self._opcoes, 1):
            print(f"{i}) {opcao}")

    def verificar_resposta(self, resposta_usuario):
        try:
            indice = int(resposta_usuario) - 1
            if indice < 0 or indice >= len(self._opcoes):
                return False
            return self._opcoes[indice].strip().lower() == self._resposta_correta.strip().lower()
        except ValueError:
            return False