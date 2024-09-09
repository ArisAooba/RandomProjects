# storage.py

import sqlite3
from models import Pergunta, Prova


class Storage:
    def __init__(self, db_name='avaliacoes.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Perguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nivel TEXT,
            tipo TEXT,
            cabecalho_pergunta TEXT,
            resposta_certa TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Provas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Provas_Perguntas (
            prova_id INTEGER,
            pergunta_id INTEGER,
            FOREIGN KEY (prova_id) REFERENCES Provas(id),
            FOREIGN KEY (pergunta_id) REFERENCES Perguntas(id)
        )
        ''')

    def salvar_pergunta(self, pergunta: Pergunta):
        self.cursor.execute('''
        INSERT INTO Perguntas (nivel, tipo, cabecalho_pergunta, resposta_certa)
        VALUES (?, ?, ?, ?)
        ''', (pergunta.nivel, pergunta.tipo, pergunta.cabecalho_pergunta, pergunta.resposta_certa))
        self.conn.commit()
        return self.cursor.lastrowid


    def salvar_prova(self, prova: Prova):
        self.cursor.execute('''
        INSERT INTO Provas (titulo)
        VALUES (?)
        ''', (prova.titulo,))
        prova_id = self.cursor.lastrowid

        for pergunta in prova.perguntas:
            pergunta_id = self.salvar_pergunta(pergunta)
            self.cursor.execute('''
            INSERT INTO Provas_Perguntas (prova_id, pergunta_id)
            VALUES (?, ?)
            ''', (prova_id, pergunta_id))

        self.conn.commit()
        return prova_id

    def fechar(self):
        self.conn.close()
