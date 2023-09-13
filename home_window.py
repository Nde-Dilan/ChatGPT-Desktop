from PyQt5.QtWidgets import QWidget

from widget_ui.home_widget_ui import Ui_home_form


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.home_ui = Ui_home_form()
        self.home_ui.setupUi(self)
