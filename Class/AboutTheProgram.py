import os
import subprocess
import ctypes
import sys
import time
import pyautogui

from PyQt6.QtWidgets import QDialog
from ui_AboutTheProgram import Ui_AboutTheProgram

class AboutTheProgram(QDialog, Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushFixMouse.clicked.connect(self.FixMouse)
        self.pushFixRegedit.clicked.connect(self.FixRegedit)

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


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AboutTheProgram()
    window.show()
    sys.exit(app.exec())
