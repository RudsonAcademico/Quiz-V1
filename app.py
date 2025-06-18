from flask import Flask, render_template, request, redirect, session, url_for
from models.quiz import Quiz
from models.perguntaMultiplaEscolha import PerguntaMultiplaEscolha

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'

# Armazenamos só dados simples na sessão
def criar_quiz():
    quiz = Quiz("Usuário")

    # Adiciona perguntas personalizadas da sessão
    perguntas_extra = session.get('perguntas_personalizadas', [])
    for p in perguntas_extra:
        quiz._perguntas.append(
            PerguntaMultiplaEscolha(p['texto'], p['opcoes'], p['resposta_correta'])
        )

    return quiz


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        session['nome'] = nome
        session['indice'] = 0
        session['pontuacao'] = 0
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    quiz = criar_quiz()
    nome = session.get('nome')
    indice = session.get('indice', 1)
    pontuacao = session.get('pontuacao', 0)

    resultado_resposta = None

    if request.method == 'POST':
        resposta = request.form['resposta']
        pergunta = quiz._perguntas[indice]
        if pergunta.verificar_resposta(resposta):
            pontuacao += 1
            resultado_resposta = 'acerto'
        else:
            resultado_resposta = 'erro'
        indice += 1
        session['indice'] = indice
        session['pontuacao'] = pontuacao

    if indice >= quiz.total_perguntas():
        return render_template('quiz.html', fim_quiz=True, resultado_resposta=resultado_resposta)

    pergunta_atual = quiz._perguntas[indice]
    texto, opcoes = pergunta_atual.exibir()
    
    return render_template('quiz.html', pergunta=texto, opcoes=opcoes, resultado_resposta=resultado_resposta, fim_quiz=False)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        texto = request.form['pergunta']
        opcoes = [
            request.form['opcao0'],
            request.form['opcao1'],
            request.form['opcao2'],
            request.form['opcao3'],
        ]
        resposta_correta = opcoes[int(request.form['correta'])-1]

        # ⚠️ Recupera lista atual com cópia para garantir persistência
        perguntas = session.get('perguntas_personalizadas', []).copy()

        # Adiciona nova pergunta
        nova_pergunta = {
            'texto': texto,
            'opcoes': opcoes,
            'resposta_correta': resposta_correta
        }
        perguntas.append(nova_pergunta)

        # ✅ Força atualização da session com nova lista
        session['perguntas_personalizadas'] = perguntas

        return redirect(url_for('adicionar'))

    return render_template('adicionar.html')



@app.route('/resultado')
def resultado():
    pontuacao = session.get('pontuacao', 0)
    quiz = criar_quiz()
    total = quiz.total_perguntas()
    return render_template('resultado.html', pontuacao=pontuacao, total=total)

if __name__ == '__main__':
    app.run(debug=True)
