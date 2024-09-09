import string

from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox,
                               QComboBox, QLabel, QMainWindow, QMessageBox,
                               QPushButton, QRadioButton, QStackedWidget,
                               QTextEdit, QToolButton, QWidget, QDialog,
                               QFormLayout, QLineEdit, QDialogButtonBox, 
                               QFileDialog)

from base import Ui_MainWindow
from models import Pergunta, Prova
from storage import Storage
from fpdf import FPDF


class TitleInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insira o Título da Prova")

        # Layout principal
        layout = QFormLayout()
        

        # Label e campo de entrada
        self.label = QLabel("Título da Prova:")
        self.label.setStyleSheet('color: #000')
        self.title_input = QLineEdit()

        layout.addRow(self.label, self.title_input)

        # Botões OK e Cancelar
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.button_box.setStyleSheet('color: #000')


        layout.addWidget(self.button_box)

        self.setLayout(layout)
        self.button_box.setStyleSheet('background-color: #ccc ')

        # self.title_input.setStyleSheet("background-color: yellow;")

    def get_title(self):
        return self.title_input.text()


class PDF(FPDF):

    def add_title(self, title):
        self.set_font('Arial', 'B', 16)  # Fonte Arial, Negrito, Tamanho 16
        self.set_xy(10, 30)  # Posiciona o título no topo da página
        self.cell(0, 10, title, ln=True, align='C')  # Título centralizado

    def header(self):
        # Adiciona a imagem no topo do PDF
        # self.image(logo_brasao_path, 10, 8, 33)  # (caminho, x, y, largura)

        self.set_xy(40, 4)  # Ajusta a posição x e y para o texto
        self.set_font('Times', '', 11)
        line_height = 4
        self.multi_cell(0, line_height, texto_2, 0, 1, 'C')

        self.image(logo_path, 10, 4, 30)  # (caminho, x, y, largura)
        self.ln(25)  # espaçamento inferior (parece um padding)

    def footer(self):
        # Posiciona o rodapé a 1.5 cm da parte inferior
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, num, title):
        self.set_font('Arial', '', 12)
        self.cell(0, 0, f'{num}) {title.capitalize()}', 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_question(self, num, question):
        self.chapter_title(num, question['cabecalho_pergunta'])
        self.chapter_body("\t\t\t\tR:")

    # Adiciona uma nova página para cada pergunta
    def gerar_gabarito(self, num, question):
        self.chapter_title(num, question['cabecalho_pergunta'])
        self.chapter_body(
            f"Nível: {question['nivel']}\nTipo: {question['tipo']}\nResposta: {question['resposta_certa']}")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.list_perguntas = []
        self.count = 1
        self.alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                         'W', 'X', 'Y', 'Z']

        # grupo para os radio buttons
        self.radio_group = QButtonGroup(self)

        # Adicionar os botões de rádio ao grupo
        self.radio_group.addButton(self.findChild(
            QRadioButton, 'FCP_radioButton_dissertativa'))  # type: ignore
        self.radio_group.addButton(self.findChild(
            QRadioButton, 'FCP_radioButton_objetiva'))  # type: ignore
        self.radio_group.addButton(self.findChild(
            QRadioButton, 'FCP_radioButton_true_or_false'))  # type: ignore

        # Inicializa o armazenamento
        self.storage = Storage()

        # Variável para armazenar a prova atual
        self.prova_atual = Prova("Prova de Exemplo")

        # Definir o QStackedWidget
        self.abas = self.findChild(QStackedWidget, 'abas')
        self.QSW_FCP = self.findChild(QStackedWidget, 'stackedWidget_FCP')

        # PAGINAS
        self.pg_GRUPO = self.findChild(QWidget, 'pg_GRUPO')
        self.pg_PROVA = self.findChild(QWidget, 'pg_PROVA')
        self.pg_criar_provas = self.findChild(QWidget, 'pg_criar_provas')
        self.pg_docente = self.findChild(QWidget, 'pg_docente')
        self.pg_turma = self.findChild(QWidget, 'pg_turma')

        # Pagina de questões
        
        self.pg_question_objetiva = self.findChild(
            QWidget, 'FCP_question_objetiva')
        self.pg_question_true_or_false = self.findChild(
            QWidget, 'FCP_question_true_or_false')
        

        # Conectando os botões para mudar de página
        self.findChild(QToolButton, 'toolButton_grupos'). \
            clicked.connect(self.show_pg_GRUPO)  # type: ignore

        self.findChild(QToolButton, 'toolButton_provas'). \
            clicked.connect(self.show_pg_PROVA)  # type: ignore

        self.findChild(QPushButton, 'pg1_btn_novo'). \
            clicked.connect(self.show_pg_criar_prova)  # type: ignore

        self.findChild(QToolButton, 'toolButton_docente'). \
            clicked.connect(self.show_pg_docente)  # type: ignore

        self.findChild(QToolButton, 'toolButton_turmas'). \
            clicked.connect(self.show_pg_turma)  # type: ignore

        # radio buttons para as abas de perguntas
        self.findChild(QRadioButton, 'FCP_radioButton_dissertativa'). \
            clicked.connect(self.show_FCP_dissertativa)  # type: ignore

        self.findChild(QRadioButton, 'FCP_radioButton_objetiva'). \
            clicked.connect(self.show_FCP_obejtiva)  # type: ignore

        self.findChild(QRadioButton, 'FCP_radioButton_true_or_false'). \
            clicked.connect(self.show_FCP_true_or_false)  # type: ignore

        # Botão para salvar a prova
        self.findChild(QPushButton, 'FCP_btn_proximo').clicked.connect(
            self.salvar_prova)  # type: ignore

        # conectar btn salvar PDF
        self.findChild(QPushButton, 'FCP_btn_gerar_pdf_dc_top_right'). \
            clicked.connect(self.salvar_pdf)  # type: ignore
        

    def show_pg_GRUPO(self):
        # Mudando para a página grupo
        self.abas.setCurrentWidget(self.pg_GRUPO)  # type: ignore

    def show_pg_PROVA(self):
        # Mudando para a página prova
        self.abas.setCurrentWidget(self.pg_PROVA)  # type: ignore

    def show_pg_criar_prova(self):
        # Mudando para a página criação de prova
        self.abas.setCurrentWidget(self.pg_criar_provas)  # type: ignore

    def show_pg_docente(self):
        # Mudando para a página docente
        self.abas.setCurrentWidget(self.pg_docente)  # type: ignore

    def show_pg_turma(self):
        # Mudando para a página turma
        self.abas.setCurrentWidget(self.pg_turma)  # type: ignore

    # defs para as abas de perguntas
    def show_FCP_dissertativa(self):
        # Mudando para a página de questões dissertativas
        self.QSW_FCP.setCurrentWidget(  # type: ignore
            self.pg_question_dissertativa)

    def show_FCP_obejtiva(self):
        # Mudando para a página de questões objetivas
        self.QSW_FCP.setCurrentWidget(
            self.pg_question_objetiva)  # type: ignore

    def show_FCP_true_or_false(self):
        # Mudando para a página de questões verdadeiro ou falso
        self.QSW_FCP.setCurrentWidget(
            self.pg_question_true_or_false)  # type: ignore

    # defs para o BD

    def show_message(self, message):
        # Cria uma instância de QMessageBox
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)  # Tipo de mensagem (aviso)
        msg_box.setWindowTitle("Aviso")        # Título da caixa de mensagem
        msg_box.setText(message)               # Mensagem a ser exibida
        msg_box.setStandardButtons(QMessageBox.Ok)  # Botões padrão
        msg_box.exec()  # Exibe a caixa de mensagem

    def get_selected_radio_button_text(self):
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            return selected_button.text()
        else:
            return "Nenhum tipo de pergunta foi selecionado."

    def obter_texto_combobox(self):
        combo_box = self.findChild(QComboBox, 'FCP_comboBox_level_question')
        if combo_box:
            texto_selecionado = combo_box.currentText()
            return texto_selecionado
        else:
            print("ComboBox não encontrado.")
            return ""

    def save_prova_dissertativa_dict(self):
        self.questions = {}
        teste = self.FP_HEADER_INFO_titulo_label.text()

        txt_resposta_certa = self.findChild(
            QTextEdit, 'FCP_QTextEdit_respost_certa'). \
            toPlainText().strip()  # type: ignore

        if not txt_resposta_certa:
            self.show_message(
                "Por favor, preencha a resposta certa para a pergunta dissertativa.")
            return
        # Criar o objeto Pergunta para dissertativa

        pergunta = Pergunta(nivel=self.nivel_selecionado, tipo=self.tipo_pergunta,
                            cabecalho_pergunta=self.txt_pergunta,
                            resposta_certa=txt_resposta_certa)

        self.questions['nivel'] = self.nivel_selecionado
        self.questions['tipo'] = self.tipo_pergunta
        self.questions['cabecalho_pergunta'] = self.txt_pergunta
        self.questions['resposta_certa'] = txt_resposta_certa

        self.list_perguntas.append(self.questions)

        return pergunta

    def save_prova_objetiva(self):
        # Obtém os widgets QCheckBox para alternativas
        checkboxes = [
            self.findChild(
                QCheckBox, 'FCP_objetiva_checkBox_resposta_certa_A'),
            self.findChild(
                QCheckBox, 'FCP_objetiva_checkBox_resposta_certa_B'),
            self.findChild(
                QCheckBox, 'FCP_objetiva_checkBox_resposta_certa_C'),
            self.findChild(
                QCheckBox, 'FCP_objetiva_checkBox_resposta_certa_D')
        ]

        # Verifica se todos os widgets foram encontrados
        if None in checkboxes:
            self.show_message(
                "Um ou mais checkboxes de alternativas não foram encontrados.")
            return

        # Obtém todas as alternativas e o estado de marcação das respostas certas
        alternativas = [checkbox.text() for checkbox in checkboxes]
        resposta_certa = [checkbox.isChecked() for checkbox in checkboxes]

        # Verifica se todas as alternativas têm texto e se exatamente uma alternativa está marcada
        if not all(alternativas):
            self.show_message("Por favor, preencha todas as alternativas.")
            return

        if not any(resposta_certa):
            self.show_message("Por favor, marque a resposta certa.")
            return

        if resposta_certa.count(True) != 1:
            self.show_message(
                "Por favor, marque exatamente uma alternativa como a resposta certa.")
            return

        # Cria o objeto Pergunta para perguntas objetivas
        resposta_certa_idx = resposta_certa.index(True)

        resposta_certa_letra = self.alfabeto[resposta_certa_idx]

        pergunta = Pergunta(
            nivel=self.nivel_selecionado,
            tipo=self.tipo_pergunta,
            cabecalho_pergunta=self.txt_pergunta,
            resposta_certa=resposta_certa_letra
        )

        return pergunta

    def save_prova_true_or_false(self):
        # Para perguntas de verdadeiro/falso, verifique a resposta certa
        resposta_certa = self.findChild(
            QRadioButton, 'FCP_QRadioButton_verdadeira').isChecked()
        if not resposta_certa and not self.findChild(QRadioButton, 'FCP_QRadioButton_falsa').isChecked():
            self.show_message(
                "Por favor, selecione a resposta certa (Verdadeira ou Falsa).")
            return

        # Criar o objeto Pergunta para verdadeira/falsa
        resposta_certa = "Verdadeira" if resposta_certa else "Falsa"
        pergunta = Pergunta(nivel=self.nivel_selecionado, tipo=self.tipo_pergunta,
                            cabecalho_pergunta=self.txt_pergunta,
                            resposta_certa=resposta_certa)

        return pergunta

    def salvar_prova(self):

        valor = self.findChild(QLabel, 'label_qtd_pergunta')

        # Obtenha o tipo de pergunta selecionado
        self.tipo_pergunta = self.get_selected_radio_button_text().strip()

        # Obtenha o cabeçalho da pergunta
        self.txt_pergunta = self.findChild(
            QTextEdit, 'FCP_QTextEdit_cabecalho').toPlainText().strip()

        # Obtenha o nível selecionado
        self.nivel_selecionado = self.obter_texto_combobox().strip()

        # Verifique se o cabeçalho da pergunta e o nível estão preenchidos
        if not self.txt_pergunta or not self.nivel_selecionado:
            self.show_message(
                "Por favor, preencha o cabeçalho da pergunta e o nivel.")
            return

        # Validações específicas para cada tipo de pergunta
        if self.tipo_pergunta == "Dissertativa":
            # pergunta = self.save_prova_dissertativa()
            pergunta = self.save_prova_dissertativa_dict()

        elif self.tipo_pergunta == "Objetiva":
            pergunta = self.save_prova_objetiva()

        elif self.tipo_pergunta == "Verdadeira/Falsa":
            pergunta = self.save_prova_true_or_false()

        # Salvando a pergunta no banco de dados
        checkbox_save_question = self.findChild(
            QCheckBox, 'FCP_checkBox_save_question')
        if checkbox_save_question.isChecked():
            pergunta_id = self.storage.salvar_pergunta(pergunta)


        self.count += 1
        valor.setText(f'Pergunta: {self.count}')  # type: ignore

        # Limpar os campos após salvar
        self.limpar_campos()

    def limpar_campos(self):
        # Limpar o QTextEdit para a pergunta

        self.findChild(QTextEdit, 'FCP_QTextEdit_cabecalho'). \
            clear()  # type: ignore

        self.findChild(QTextEdit, 'FCP_QTextEdit_respost_certa'). \
            clear()  # type: ignore

        # Limpar o QComboBox (opcional, se você deseja redefinir a seleção)

        self.findChild(
            QComboBox, 'FCP_comboBox_level_question'). \
            setCurrentIndex(0)  # type: ignore

        # Limpar a seleção dos QRadioButtons (se estiver usando um QButtonGroup)
        self.radio_group.setExclusive(False)  # Permite limpar a seleção
        if self.radio_group.checkedButton():
            self.radio_group.checkedButton().setChecked(
                True)  # Desmarcar o botão selecionado
        self.radio_group.setExclusive(True)  # Restaura a exclusividade

    def closeEvent(self, event):
        # Fechar a conexão com o banco de dados ao sair
        self.storage.fechar()
        super().closeEvent(event)

    def open_title_dialog(self):
        dialog = TitleInputDialog(self)
        if dialog.exec() == QDialog.Accepted:  # type: ignore
            title = dialog.get_title()

        return title

    def salvar_pdf(self):
        # Gerar o PDF da prova
        title = self.open_title_dialog()
        
        # Abrir diálogo para escolher onde salvar a prova em PDF
        save_path, _ = QFileDialog.getSaveFileName(None, 'Salvar Prova', '', "PDF Files (*.pdf);;All Files (*)")

        if save_path:
            # Gerar o PDF da prova
            prova_pdf = PDF()
            prova_pdf.add_page()

            for num, question in enumerate(self.list_perguntas):
                prova_pdf.add_question(num + 1, question)

            # Salvar o PDF da prova no local escolhido
            prova_pdf.output(save_path)
            
            # Gerar o PDF do gabarito
            gabarito_pdf = PDF()
            gabarito_pdf.add_page()

            for num, question in enumerate(self.list_perguntas):
                gabarito_pdf.gerar_gabarito(num + 1, question)

            gabarito_pdf.add_title('Gabarito')
            
            # Salvar o gabarito no mesmo local, só que com "Gabarito_" no nome
            gabarito_save_path = save_path.replace('.pdf', f'_Gabarito.pdf')
            gabarito_pdf.output(gabarito_save_path)

            self.show_message('PDFs gerados com sucesso!')



if __name__ == '__main__':
    texto = '''
    SERVIÇO PÚBLICO FEDERAL
    MINISTÉRIO DA EDUCAÇÃO INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PARÁ - IFPA
    PRÓ-REITORIA DE PESQUISA, PÓS-GRADUAÇÃO E INOVAÇÃO'''

    texto_2 = """
    Instituto Federal de Educação, Ciência e Tecnologia do Pará
    Campus Altamira
    Professor: Gilberto de Melo
    Curso: TADS
    Disciplica: REDES II
    Aluno(a):____________________________________________________________"""

    logo_path = 'img/logo_ifpa_2.png'
    logo_brasao_path = 'img/brasaooficialcolorido.png'

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

