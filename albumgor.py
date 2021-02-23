from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3
import ast

from albumbilgigor import albumbilgi

class albumler(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("albumler.ui", self)

        self.username = ""
        self.sarkiSayac = 0
        self.platformSayac = 0

        self.vt = sqlite3.connect("musiclib_vt.db")
        self.cur = self.vt.cursor()

        self.albumbilgisi = albumbilgi()

        self.albumeGit.clicked.connect(self.albumBilgi)

    def albumBilgi(self):
        secili = self.albumListe.currentRow()
        album = self.albumListe.item(secili)

        if album is None:
            return

        albumAd = album.text()
        albumBilgiler = self.cur.execute("""SELECT * FROM albumler WHERE albumAd = '{}'""".format(albumAd)).fetchone()

        self.albumbilgisi.albumad_label.setText(albumAd)
        self.albumbilgisi.turad_label.setText(albumBilgiler[2])
        sarkilar = ast.literal_eval(albumBilgiler[3])
        self.albumbilgisi.album_sarkilar.clear()
        while (self.sarkiSayac < len(sarkilar)):
            key = str(self.sarkiSayac+1)
            self.albumbilgisi.album_sarkilar.addItem(sarkilar[key])
            self.sarkiSayac += 1
        platformlar = ast.literal_eval(albumBilgiler[4])
        self.albumbilgisi.album_platform.clear()
        while (self.platformSayac < len(platformlar)):
            self.albumbilgisi.album_platform.addItem(platformlar[self.platformSayac])
            self.platformSayac +=1

        self.albumbilgisi.show()
        self.platformSayac = 0
        self.sarkiSayac = 0


        