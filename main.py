from models.quiz import Quiz
def main():
    quiz = Quiz()

    # Cadastra usuário
    nome = input("Digite seu nome para iniciar o quiz: ")
    quiz.cadastrar_usuario(nome)

    # Carrega perguntas padrão
    quiz.carregar_perguntas_padrao()

    # Permite adicionar novas perguntas
    while True:
        escolha = input("\nDeseja adicionar uma nova pergunta? (s/n): ").strip().lower()
        if escolha == "s":
            quiz.cadastrar_perguntas_interativamente()
        elif escolha == "n":
            break
        else:
            print("Digite 's' para sim ou 'n' para não.")

    # Inicia o quiz com TODAS as perguntas
    quiz.iniciar()

if __name__ == "__main__":
    main()