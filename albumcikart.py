from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3

class albumcikart(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("albumcikart.ui", self)

        self.username = ""
        self.sarkilar = {}
        self.sayac = 0
        self.platformListe = []

        self.vt = sqlite3.connect("musiclib_vt.db")
        self.cur = self.vt.cursor()

        self.isSingle_check.stateChanged.connect(self.Checkbox)
        self.sarkiekle_buton.clicked.connect(self.listeyeEkle)
        self.sarkicikart_buton.clicked.connect(self.listedenCikart)
        self.pekle_buton.clicked.connect(self.platformEkle)
        self.pcikart_buton.clicked.connect(self.platformCikart)
        self.albumcikart_buton.clicked.connect(self.Done)

    
    def Checkbox(self):
        if(self.isSingle_check.isChecked() == True):
            self.sarkiad_input.setEnabled(False)
            self.sarkiekle_buton.setEnabled(False)
        elif(self.isSingle_check.isChecked() == False):
            self.sarkiad_input.setEnabled(True)
            self.sarkiekle_buton.setEnabled(True)
    
    def listeyeEkle(self):
        sarkiAd = self.sarkiad_input.text()
        self.sarkiListe.addItem(sarkiAd)
        self.sayac += 1
        self.sarkilar[str(self.sayac)] = sarkiAd
    
    def listedenCikart(self):
        secili = self.sarkiListe.currentRow()
        sarki = self.sarkiListe.item(secili)

        if sarki is None:
            return
        
        sarki = self.sarkiListe.takeItem(secili)
        del self.sarkilar[str(secili+1)]
        del sarki
        self.sayac -= 1

    def platformEkle(self):
        secili = self.platformList.currentRow()
        platform = self.platformList.item(secili)

        if platform is None:
            return
        
        platformAd = platform.text()
        self.platformlar.addItem(platformAd)
        platform = self.platformList.takeItem(secili)
        del platform

        self.platformListe += [platformAd]

    def platformCikart(self):
        secili = self.platformlar.currentRow()
        platform = self.platformlar.item(secili)

        if platform is None:
            return

        platformAd = platform.text()
        self.platformList.addItem(platformAd)
        platform = self.platformlar.takeItem(secili)
        del platform

        self.platformListe.remove(platformAd)
    
    def Done(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS albumler (username, albumAd, tur, sarkilar, platformlar)""")
        username = self.username
        albumAd = self.album_input.text()
        if(self.isSingle_check.isChecked() == True):
            self.sarkilar = {"1": albumAd}
            sarkiList = self.sarkilar
        else:
            sarkiList = self.sarkilar
        tur = self.tur_combo.currentText()
        platformlar = self.platformListe
        self.cur.execute("""INSERT INTO albumler VALUES (?, ?, ?, ?, ?)""", (username, albumAd, tur, str(sarkiList), str(platformlar)))
        self.vt.commit()
        self.close()