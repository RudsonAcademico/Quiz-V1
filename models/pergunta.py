from abc import ABC, abstractmethod

# Classe base para perguntas
class Pergunta(ABC):
    def __init__(self, texto, resposta_correta):
        self._texto = texto
        self._resposta_correta = resposta_correta

    @abstractmethod
    def exibir(self):
        pass

    @abstractmethod
    def verificar_resposta(self, resposta_usuario):
        pass