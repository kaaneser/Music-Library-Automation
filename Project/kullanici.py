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