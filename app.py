import sys
import os, json

from PyQt5.QtWidgets import QApplication

from main_app import MainWindow

if __name__ == '__main__':
    flag = os.path.exists("datas/data.json")
    if not flag:
        os.mkdir("datas")
        with open("datas/data.json","w") as f:
            f.write(json.dumps([]))
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
#INFO: if there's a problem go to main_ui.py and change import ressource_rc to from static import ressource_rc and replace it everywhere

    sys.exit(app.exec())