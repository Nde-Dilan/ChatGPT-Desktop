from PyQt5.QtWidgets import QWidget

from widget_ui.home_widget_ui import Ui_home_form


class HomeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.home_ui = Ui_home_form()
        self.home_ui.setupUi(self)
