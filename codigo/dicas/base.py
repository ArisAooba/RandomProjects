
from PySide6.QtWidgets import QMainWindow

from nome_do_arquivo.ui import QApplication, Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Titulo')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    window.autoFillBackground()
    app.exec()
