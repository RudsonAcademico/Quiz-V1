from models.usuario import Usuario
from models.perguntaMultiplaEscolha import PerguntaMultiplaEscolha


class Quiz:
    def __init__(self):
        self._perguntas = []
        self._usuario = None

    def cadastrar_usuario(self, nome):
        self._usuario = Usuario(nome)

    def adicionar_pergunta(self, pergunta):
        self._perguntas.append(pergunta)

    def carregar_perguntas_padrao(self):
        self.adicionar_pergunta(PerguntaMultiplaEscolha(
            "Qual a capital do Brasil?",
            ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
            "Brasília"
        ))
        self.adicionar_pergunta(PerguntaMultiplaEscolha(
            "Quem escreveu 'Dom Casmurro'?",
            ["Machado de Assis", "Carlos Drummond", "Clarice Lispector", "Monteiro Lobato"],
            "Machado de Assis"
        ))
        self.adicionar_pergunta(PerguntaMultiplaEscolha(
            "Quanto é 9 x 7?",
            ["56", "63", "72", "69"],
            "63"
        ))

    def cadastrar_perguntas_interativamente(self):
        print("\n=== Cadastro de Nova Pergunta ===")
        texto = input("Digite o texto da pergunta: ")
        opcoes = []
        for i in range(4):
            opcao = input(f"Digite a opção {i+1}: ")
            opcoes.append(opcao)
        while True:
            resposta = input("Digite o número da alternativa correta (1-4): ")
            if resposta in ["1", "2", "3", "4"]:
                resposta_correta = opcoes[int(resposta) - 1]
                break
            else:
                print("Entrada inválida. Digite um número de 1 a 4.")
        nova = PerguntaMultiplaEscolha(texto, opcoes, resposta_correta)
        self.adicionar_pergunta(nova)
        print("✅ Pergunta adicionada com sucesso!")

    def iniciar(self):
        if not self._usuario:
            print("Usuário não cadastrado!")
            return

        print(f"\nBem-vindo ao quiz, {self._usuario.get_nome()}!")
        for pergunta in self._perguntas:
            pergunta.exibir()
            resposta = input("Digite o número da resposta: ")
            if pergunta.verificar_resposta(resposta):
                print("✔️ Resposta correta!")
                self._usuario.adicionar_ponto()
            else:
                print("❌ Resposta incorreta.")

        print(f"\nPontuação final: {self._usuario.get_pontuacao()} de {len(self._perguntas)}")