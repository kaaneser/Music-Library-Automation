from PyQt5.QtWidgets import QApplication
from anasayfa import MainPage

app = QApplication([])
window = MainPage()
window.show()
app.exec_()