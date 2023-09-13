import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QListWidgetItem, QStyledItemDelegate, \
    QStyle, QWidget, QHBoxLayout, QLineEdit, QAction, QSpacerItem, QSizePolicy, QGridLayout, QLabel, QFrame, \
    QVBoxLayout, QItemDelegate, QDialogButtonBox, QListView, QAbstractItemView

from PyQt5.QtCore import pyqtSlot, QSize, QStringListModel, QPoint, Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from widget_ui.main_ui import Ui_MainWindow
from home_window import HomeWindow
from chat_window import ChatWindow
from connect_db import connectDB
import open_ai_chat


# TODO: Convert all the ui files to python code and store them inside the widget_ui directory


class CustomWidget(QWidget):
    ## Create each chat in chat list
    def __init__(self, text, show_btn_flag,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #  Create layout for chat title
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5,0,0,0)

        # Create icon widget of chat title

        chat_icon = QIcon("static/icons/chat-left.svg")
        chat_icon_btn = QPushButton(self)
        chat_icon_btn.setIcon(chat_icon)

        # Create title widget to show title

        chat_title = QLineEdit(self)
        chat_title.setText(text)
        chat_title.setReadOnly(True)

        # Create delete and edit buttons for chat title
        delete_icon = QIcon("static/icons/delete.svg")
        delete_btn = QPushButton(self)
        delete_btn.setIcon(delete_icon)

        edit_icon = QIcon("static/icons/edit.svg")
        edit_btn = QPushButton(self)
        edit_btn.setIcon(edit_icon)

        # Style for QPushButton inside the chat list

        style_str = """
        QPushButton {
            border:none;
            max-height:20px;
            max-width:20px;
            background:transparent;
        }"""
        # Style for QLineEdit inside the chat list

        chat_title_style_str = """
        QLineEdit {
            border:none;
            color:#fff;
            background:transparent;
            font-size:15px;
            padding-left:2px;
        }
        """
        chat_title.setStyleSheet(chat_title_style_str)
        edit_btn.setStyleSheet(style_str)
        delete_btn.setStyleSheet(style_str)
        chat_icon_btn.setStyleSheet(style_str)


        # Check if be selected. if that hide delete and edit buttons in chat list

        if not show_btn_flag:
            delete_btn.hide()
            edit_btn.hide()

        # Add all the widget of the chat title into layout

        layout.addWidget(chat_icon_btn)
        layout.addWidget(delete_btn)
        layout.addWidget(edit_btn)
        layout.addWidget(chat_title)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialization of the main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Instantiate the database object
        self.connect_db = connectDB()

        # Get objects from main window
        self.message_input = self.ui.input_textEdit
        self.input_frame = self.ui.input_frame
        self.new_chat_btn = self.ui.new_chat_btn
        self.send_message_btn = self.ui.send_btn
        self.main_scroll_area = self.ui.scrollArea
        self.clear_conversations_btn = self.pushButton
        self.log_out_btn = self.pushButton_6

        # Hide scrollbar of main scroll area
        self.main_scroll_area.setVerticalScrollBarPolicy(1)

        # Resize input frame and textEdit

