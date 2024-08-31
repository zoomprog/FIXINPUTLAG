import os
import subprocess
import ctypes
import sys
from PyQt6.QtWidgets import QDialog
from ui_AboutTheProgram import Ui_AboutTheProgram

class AboutTheProgram(QDialog, Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushFixMouse.clicked.connect(self.FixMouse)

    def FixMouse(self):
        # Get the absolute path to the batch file
        batch_file_path = os.path.join('FileFixInputLag', 'FixMouse', 'Mouse.bat')

        # Execute the batch file
        subprocess.run(batch_file_path, shell=True)

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AboutTheProgram()
    window.show()
    sys.exit(app.exec())
