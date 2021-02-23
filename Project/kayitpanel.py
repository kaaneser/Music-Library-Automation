from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3

from kullanicipanel import kullanicikp

class Kullanici():
    isim = ""
    username = ""
    password = ""

    def __init__(self, isim, username, password):
        self.isim = isim
        self.username = username
        self.password = password
        self.vt = sqlite3.connect("musiclib_vt.db")
        self.cur = self.vt.cursor()

class giris(QWidget):

    def __init__(self):
        super().__init__()

        loadUi("girisyap.ui", self)

        self.kayitolButon.clicked.connect(self.kayitVeritabani)
        self.girisyapButon.clicked.connect(self.girisVeritabani)

        self.kullanicipanel = kullanicikp()
    
    def kayitVeritabani(self):
        
        isim = self.isim_input.text()
        username = self.kaykadi_input.text()
        password = self.kaysifre_input.text()
        kullanici = Kullanici(isim, username, password)
        kullanici.cur.execute("""CREATE TABLE IF NOT EXISTS users (ad, username, password)""")
        isRegistered = kullanici.cur.execute("""SELECT * FROM users WHERE username = '{}'""".format(username)).fetchone()
        if (isRegistered != None):
            self.regInfo.setText("K. Adı Alınmış, Tekrar Dene")
        else:
            kullanici.cur.execute("""INSERT INTO users VALUES (?, ?, ?)""", (isim, username, password))
            kullanici.vt.commit()
            self.regInfo.setText("Başarıyla kaydolundu!")
    
    def girisVeritabani(self):

        username = self.kadi_input.text()
        password = self.sifre_input.text()
        kullanici = Kullanici("", username, password)
        login = kullanici.cur.execute("""SELECT * FROM users WHERE username = '{}'""".format(username)).fetchone()
        if (login == None):
            self.logInfo.setText("Kullanıcı bulunamadı!")
        else:
            if (login[2] != password):
                self.logInfo.setText("Hatalı K.Adı / Şifre!")
            else:
                self.kullanicipanel.show()
                self.kullanicipanel.hosgeldiniz.setText("Hoşgeldiniz, {}".format(login[0]))
                self.kullanicipanel.username = username
                self.close()
        