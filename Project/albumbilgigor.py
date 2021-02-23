from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3
import ast

class albumbilgi(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("albumbilgisi.ui", self)

        self.tamamButon.clicked.connect(self.Tamam)
    
    def Tamam(self):
        self.close()

        
        




        