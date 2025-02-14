import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, 
QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
 QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from pygame import mixer 


from ui_splash_screen import Ui_SplashScreen


counter = 0


class MainWindow(QMainWindow):
    def __init__(self):
        print("É bom de mais Junior")

class SplashScreen(QMainWindow):
    def __init__(self):
       
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
       
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        self.ui.label_description.setText("Seja bem Vindo <strong>Jogador</strong>")

        self.show()

    def progress(self):

        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            mixer.init()
            mixer.music.load("./sons/inicio.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            # STOP TIMER
            self.timer.stop() 
            import login       
            self.close()

        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())