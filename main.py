import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
import Class.AboutTheProgram
# GUI FILE
from splash_screen import Ui_SplashScreen
import icon


class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()


        self.setupUi(self)
        self.show()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # APPLY DROP SHADOW EFFECT
        self.circularBg.setStyleSheet("""
            QFrame {
                border-radius: 150px;
                background-color: rgba(77, 77, 127, 60);
            }
        """)

        # Создание таймера
        self.timer = QtCore.QTimer()
        # Подключение сигнала timeout к слоту progress
        self.timer.timeout.connect(self.progress)
        # Запуск таймера с интервалом в миллисекундах
        self.timer.start(20)

        # Инициализация счетчика
        self.counter = 0



    def progress(self):
        value = self.counter
        # Установить значение для progressBar
        self.progressBarValue(value)
        # Закрыть экран загрузки и открыть основное приложение
        if self.counter > 100:
            # Остановить таймер
            self.timer.stop()

            # Показать главное окно
            self.ui = Class.AboutTheProgram.AboutTheProgram()
            self.ui.show()

            # Закрыть экран загрузки
            self.close()

        # Увеличить счетчик
        self.counter += 1

    def progressBarValue(self, value):
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 128, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.circularProgress.setStyleSheet(newStylesheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SplashScreen()
    mainWindow.show()
    sys.exit(app.exec())