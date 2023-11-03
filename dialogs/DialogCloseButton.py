from typing import Optional
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QDialog, QVBoxLayout, QGridLayout, QPushButton, QLabel

Stylesheet = """
#Main_Widget {{
    border-radius: 16px;
    background: {};
}}

#Title {{
    font-family: Helvetica;
    font-weight: bold;
    font-size: 20px;
    padding: 24px;
    padding-left: 20px;
}}
#Content {{
    font-family: Helvetica;
    font-size: 16px;
    padding-left: 24px;
    padding-right: 24px;
    padding-bottom: 24px;
}}

#closeButton {{
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

#closeButton:hover {{
    background: rgba(33, 43, 54, 0.8);
}}

"""

class DialogCloseButton(QDialog):
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

        self.content = QLabel(content)
        self.content.setObjectName("Content")
        self.content.setWordWrap(True)

        # Add user interface to widget
        layout = QGridLayout(self.widget)
        # layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        layout.addWidget(self.title, 0, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.content, 1, 0)


        self.close_button = QPushButton("Close")
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.accept)
        self.close_button.setCursor(Qt.CursorShape.PointingHandCursor)

        button_box_layout = QHBoxLayout()
        
        button_box_layout.addWidget(self.close_button)
        layout.addLayout(button_box_layout, 2, 0, Qt.AlignmentFlag.AlignRight)

    def sizeHint(self):
        return QSize(600, 200)        

