import os
import subprocess
import ctypes
import sys
import time
import pyautogui
from PyQt6.QtGui import QMouseEvent, QIcon

from PyQt6.QtWidgets import QDialog, QApplication, QVBoxLayout
from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6 import QtCore
from ui_AboutTheProgram import Ui_AboutTheProgram
from Function.ScheduleInputLags.ScheduleInputLags import ScheduleWindow

class AboutTheProgram(QDialog, Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("FixInputLag")
        self.setWindowIcon(QIcon(r"C:\Users\rrarr\PycharmProjects\FIXINPUTLAG\Icons\logo.ico"))
        self.pushFixMouse.clicked.connect(self.FixMouse)
        self.pushFixRegedit.clicked.connect(self.FixRegedit)
        self.pushFixInternet.clicked.connect(self.FixInternet)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.pushCross.clicked.connect(self.CloseWindow)
        self.pushRollup.clicked.connect(self.Rollup)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.pushButton_3.clicked.connect(self.CheackInputLag)


    def FixMouse(self):
        batch_file_path = os.path.join('FileFixInputLag', 'FixMouse', 'Mouse.bat')
        subprocess.run(batch_file_path, shell=True)


    def FixRegedit(self):
        bat_files = [
            ('DecreaseDelay.bat', 'nopause'),
            ('DisableDeliveryOptimization.bat', 'nopause'),
            ('DisableDownloadMapsManager.bat', None),
            ('DisableLargeSystemCache.bat', None),
            ('DisableNagle_sAlgorithm.bat', None),
            ('DisableNetworkThrottling.bat', None),
            ('DisableNetworkThrottlingIndex.bat', None),
            ('DisableOneDriveSync.bat', None),
            ('DisablePrintingServices.bat', None),
            ('DisableSearchIndexing.bat', None),
            ('DisableSyncHost.bat', None),
        ]
        # Устанавливаем кодировку один раз
        subprocess.run(['chcp', '65001'], shell=True)
        # Выполняем бат-файлы
        for bat_file, arg in bat_files:
            bat_path = os.path.join('FileFixInputLag', 'FixRegedit', bat_file)
            if arg:
                subprocess.run([bat_path, arg], shell=True)
            else:
                subprocess.run(bat_path, shell=True)
        reg_files = [
            'FileFixInputLag/FixRegedit/Disable SysMain (Prefetch).reg',
            'FileFixInputLag/FixRegedit/Disable Telemtry _ Data Collection.reg'
        ]
        for reg_file in reg_files:
            try:
                # Выполнение команды для применения .reg файла
                result = subprocess.run(['regedit', '/s', reg_file], check=True)
                print(f"Файл {reg_file} успешно применен.")
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при применении файла {reg_file}: {e}")

    def FixInternet(self):
        bat_files = [
            ('DecreasePing.bat', None),
            ('DisableNagle_sAlgorithm.bat', None),
            ('DisableRSC.bat', None),
            ('DisableTCPRSS.bat', None),
            ('EnbleECNCapability.bat', None),
            ('StopNetworkThrottlingCommand.bat', None),
            ('TCPSetup.bat', None),
            ('TCPTune.bat', None),
        ]
        # Устанавливаем кодировку один раз
        subprocess.run(['chcp', '65001'], shell=True)
        # Выполняем бат-файлы
        for bat_file, arg in bat_files:
            bat_path = os.path.join('FileFixInputLag', 'FixInternet', bat_file)
            if arg:
                subprocess.run([bat_path, arg], shell=True)
            else:
                subprocess.run(bat_path, shell=True)

    @staticmethod
    def CloseWindow(self):
        sys.exit()

    def Rollup(self):
        self.showMinimized()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.up_bar.underMouse():
            self.offset = event.pos()
        else:
            self.offset = None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton and self.up_bar.underMouse():
            self.move(self.mapToGlobal(event.pos() - self.offset))
        else:
            self.offset = None

    def CheackInputLag(self):
        self.frame_5_layout = QVBoxLayout(self.frame_5)
        self.Shedule = ScheduleWindow()
        self.frame_5_layout.addWidget(self.Shedule)

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = AboutTheProgram()
    window.setWindowIcon(QIcon(r"C:\Users\rrarr\PycharmProjects\FIXINPUTLAG\Icons\logo.ico"))
    window.show()
    sys.exit(app.exec())
