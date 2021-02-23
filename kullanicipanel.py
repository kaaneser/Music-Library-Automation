from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3

from albumcikart import albumcikart
from albumgor import albumler

class kullanicikp(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("kullanicipaneli.ui", self)

        self.username = ""

        self.vt = sqlite3.connect("musiclib_vt.db")
        self.cur = self.vt.cursor()

        self.sarkicikartButon.clicked.connect(self.sarkiCikart)
        self.sarkigorButon.clicked.connect(self.sarkiGor)

        self.albumcikart_git = albumcikart()
        self.albumgor_git = albumler()

    def sarkiCikart(self):
        self.albumcikart_git.username = self.username
        self.albumcikart_git.show()
    
    def sarkiGor(self):
        kullanici_Albumler = self.cur.execute("""SELECT * FROM albumler WHERE username = '{}'""".format(self.username)).fetchall()

        self.albumgor_git.albumListe.clear()

        for i in range(len(kullanici_Albumler)):
            albumAd = kullanici_Albumler[i][1]
            self.albumgor_git.albumListe.addItem(albumAd)
        self.albumgor_git.username = self.username
        self.albumgor_git.show()
