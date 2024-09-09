# models.py

class Pergunta:
    def __init__(self, nivel, tipo, cabecalho_pergunta, resposta_certa):
        self.nivel = nivel
        self.tipo = tipo
        self.cabecalho_pergunta = cabecalho_pergunta
        self.resposta_certa = resposta_certa


class Prova:
    def __init__(self, titulo):
        self.titulo = titulo
        self.perguntas = []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

class turma:
    def __init__(self, nome):
        self.nome = nome

    def adicionar_nome(self, nome):
        self.nome.append(nome)