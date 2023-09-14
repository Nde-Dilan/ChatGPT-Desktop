from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy

from widget_ui.input_widget_ui import Ui_Form as Input_Form
from widget_ui.out_widget_ui import Ui_Form as Out_Form


class InputWidget(QWidget):

    def __init__(self, parent=None, chat_obj=None):
        super().__init__(parent)

        self.input_ui = Input_Form()
        self.input_ui.setupUi(self)

        self.chat_obj = chat_obj

        self.input_label = self.input_ui.label_2
        self.edit_btn = self.input_ui.pushButton

        self.edit_btn.clicked.connect(self.set_edit_text)

    def set_input_text(self, input_str):
        self.input_label.setText(input_str)

    def set_edit_text(self):
        text = self.input_label.text()
        self.chat_obj.setPlainText(text)


class OutWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.out_ui = Out_Form()
        self.out_ui.setupUi(self)

        self.out_label = self.out_ui.label_2

    def set_output_text(self, out_str):
        self.out_label.setText(out_str)


class ChatWindow(QWidget):

    def __init__(self, parent=None, chat_obj=None, chat_data=None):
        super().__init__(parent)

        self.chat_obj = chat_obj
        self.chat_data = chat_data

        self.main_verticalLayout = QVBoxLayout(self)
        self.main_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_verticalLayout.setSpacing(0)

        self.setObjectName("main_verticalLayout")

        self.style_str = """
        QPushButton,
        QLAbel {
        border:none;
        padding:5px;
        }
        QWidget{
        background:#fff;
        }
        """
        self.setStyleSheet(self.style_str)

        self.chats_data = {
            "title": "",
            "chat_list": []
        }

        if self.chat_data:
            self.chats_data["title"] = self.chat_data["title"]
            self.chats_data["chat_list"] += self.chat_data["chat_list"]

        self.show_chats()

    def show_chats(self):
        chat_list = self.chats_data.get("chat_list")
        for chat in chat_list:
            input_str = chat.get("input_str")
            input_widget = InputWidget(chat_obj=self.chat_obj)
            input_widget.set_input_text(input_str)
            self.main_verticalLayout.addWidget(input_widget)

            out_str = chat.get("out_str")
            out_widget = OutWidget()
            out_widget.set_output_text(out_str)
            self.main_verticalLayout.addWidget(out_widget)

        spacer_item = QSpacerItem(20, 293, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_verticalLayout.addWidget(spacer_item)
        self.setLayout(self.main_verticalLayout)
