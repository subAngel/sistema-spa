import sys
from PyQt5 import QtWidgets

def programa():
    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QWidget()
    boton = QtWidgets.QPushButton("Click here!")
    texto = QtWidgets.QLabel("Hello world!!")
    formato_1 = QtWidgets.QHBoxLayout()
    formato_1.addStretch()
    formato_1.addWidget(texto)
    formato_1.addStretch()

    formato_2 = QtWidgets.QVBoxLayout()
    formato_2.addWidget(boton)
    formato_2.addLayout(formato_1)

    ventana.setLayout(formato_2)

    ventana.setWindowTitle("Python con layout")
    ventana.show()

    sys.exit(app.exec_())
programa()
