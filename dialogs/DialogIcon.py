from typing import Optional
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QDialog, QVBoxLayout, QGridLayout, QPushButton, QLabel

import os

Stylesheet = """
#Main_Widget {{
    border-radius: 16px;
    background: {};
}}

#Icon {{
    padding-left: 24px;
}}

#Title {{
    font-family: Helvetica;
    font-weight: bold;
    font-size: 20px;
    padding-left: 12px;
}}

#Content {{
    font-family: Helvetica;
    font-size: 16px;
    padding-left: 24px;
    padding-right: 24px;
    padding-bottom: 24px;
    padding-top: 24px;
}}

#acceptButton {{
    font-weight: bold;
    font-family: Helvetica;
    font-size: 12px;
    color: white;
    border-radius: 5px;
    background: rgb(33, 43, 54);
    min-width: auto;
    min-height: auto;
    padding-left: 12px;
    padding-right: 12px;
    padding-top: 0px;
    padding-bottom: 0px;
    margin-left: 12px;
    margin-right: 24px;
    margin-bottom: 24px;
}}

#acceptButton:hover {{
    background: rgba(33, 43, 54, 0.8);
}}

#rejectButton {{
    font-weight: bold;
    font-family: Helvetica;
    font-size: 12px;
    border: 1px solid rgba(145, 158, 171, 0.32);
    border-radius: 5px;
    color: rgb(33, 43, 54);
    min-width: auto;
    min-height: auto;
    padding-left: 12px;
    padding-right: 12px;
    padding-top: 0px;
    padding-bottom: 0px;
    margin-bottom: 24px;
}}

#rejectButton:hover {{
    border: 1px solid rgb(33, 43, 54);
    background: rgba(33, 43, 54, 0.1);
}}
"""

basedir = os.path.dirname(__file__)


class DialogIcon(QDialog):
    def __init__(self, 
                 title: str, 
                 content: str,
                 background_color: str = "white"):
        super().__init__()
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet.format(background_color))
        self.initUi(title, content)
        
    def initUi(self, title, content):
    #     # Important: this widget is used as background and for rounded corners.
    # Main widget which contains all layouts
        self.widget = QWidget(self)
        self.widget.setObjectName('Main_Widget')
        #Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.widget)

        # Add user interface to widget
   
        self.title = QLabel(title)
        self.title.setObjectName("Title")
    
        self.icon = QLabel()
        self.icon.setPixmap(QPixmap(os.path.join(basedir, "hacker.png")))
        self.icon.setObjectName("Icon")

        title_box_layout = QHBoxLayout()
        title_box_layout.setSpacing(0)
        title_box_layout.addWidget(self.icon)
        title_box_layout.addWidget(self.title)


        self.content = QLabel(content)
        self.content.setObjectName("Content")
        self.content.setWordWrap(True)

        # Add user interface to widget
        layout = QGridLayout(self.widget)
        # layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addLayout(title_box_layout, 0, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.content, 1, 0)


        self.reject_button = QPushButton("Disagree")
        self.reject_button.setObjectName("rejectButton")
        self.reject_button.clicked.connect(self.reject)
        self.reject_button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.accept_button = QPushButton("Agree")
        self.accept_button.setObjectName("acceptButton")
        self.accept_button.clicked.connect(self.accept)
        self.accept_button.setCursor(Qt.CursorShape.PointingHandCursor)

        button_box_layout = QHBoxLayout()

        button_box_layout.addWidget(self.reject_button)
        button_box_layout.addWidget(self.accept_button)
        layout.addLayout(button_box_layout, 2, 0, Qt.AlignmentFlag.AlignRight)

    def sizeHint(self):
        return QSize(600, 200)        

