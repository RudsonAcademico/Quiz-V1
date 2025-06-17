from models.usuario import Usuario
from models.perguntaMultiplaEscolha import PerguntaMultiplaEscolha

class Quiz:
    def __init__(self, usuario_nome):
        self._usuario = Usuario(usuario_nome)
        self._perguntas = []
        self._indice_atual = 0
        self.carregar_perguntas()

    def carregar_perguntas(self):
        self._perguntas.append(PerguntaMultiplaEscolha(
            "Qual a capital do Brasil?",
            ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
            "Brasília"
        ))
        self._perguntas.append(PerguntaMultiplaEscolha(
            "Quanto é 5 x 7?",
            ["30", "35", "40", "25"],
            "35"
        ))

    def get_pergunta_atual(self):
        if self._indice_atual < len(self._perguntas):
            return self._perguntas[self._indice_atual]
        return None

    def responder(self, resposta_indice):
        pergunta = self.get_pergunta_atual()
        if pergunta and pergunta.verificar_resposta(resposta_indice):
            self._usuario.adicionar_ponto()
        self._indice_atual += 1

    def terminou(self):
        return self._indice_atual >= len(self._perguntas)

    def get_pontuacao(self):
        return self._usuario.get_pontuacao()

    def total_perguntas(self):
        return len(self._perguntas)