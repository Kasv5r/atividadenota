from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from cnindex import converterData
from modinserir import inserir

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("tela.ui")
        self.componentes()
    
    def componentes(self):
        self.caixaData = self.tela.findChild(QtWidgets.QDateEdit, "caixaData")
        self.caixaNome = self.tela.findChild(QtWidgets.QLineEdit, "caixaNome")
        self.caixaOri = self.tela.findChild(QtWidgets.QLineEdit, "caixaOri")
        self.caixaDest = self.tela.findChild(QtWidgets.QLineEdit, "caixaDest")
        self.caixaPagamento = self.tela.findChild(QtWidgets.QComboBox, "caixaPagamento")
        self.btnCadastrar = self.tela.findChild(QtWidgets.QPushButton, "btnCadastra")
        self.btnCadastrar.clicked.connect(self.cadastrarProducao)


    def cadastrarProducao(self):
        pdt = self.caixaData.text()
        name = self.caixaNome.text()
        ori = self.caixaOri.text()
        dest = self.caixaDest.text()
        fpgmt = self.caixaPagamento.currentText()
        inserir(converterData(pdt), name, ori, dest, fpgmt)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.showMaximized()
    app.exec()