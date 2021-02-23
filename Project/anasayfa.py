from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from kayitpanel import giris

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("anasayfa.ui", self)

        self.giris_buton.clicked.connect(self.kayitPencere)

        self.girisyap = giris()

    def kayitPencere(self):
        self.girisyap.show()
        self.close()