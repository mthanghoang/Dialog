import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton

from dialogs import Dialog, DialogCloseButton, DialogIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.widget = QWidget(self)
        layout = QHBoxLayout(self.widget)

        button_1 = QPushButton("Normal dialog")
        button_1.clicked.connect(self.button_1_clicked)
        
        button_2 = QPushButton("Dialog with Close button")
        button_2.clicked.connect(self.button_2_clicked)

        button_3 = QPushButton("Dialog with Icon")
        button_3.clicked.connect(self.button_3_clicked)

        layout.addWidget(button_1)
        layout.addWidget(button_2)
        layout.addWidget(button_3)
        
        self.setCentralWidget(self.widget)

    
    def button_1_clicked(self, s):
        title = "Use Google's location service?"
        content = "Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running."
        dlg = Dialog(title, content)
        dlg.exec()  # create an entirely new event loop

    def button_2_clicked(self, s):
        title = "Lorem Ipsum"
        content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        dlg = DialogCloseButton(title, content)
        dlg.exec()

    def button_3_clicked(self, s):
        title = "Lorem Ipsum"
        content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        dlg = DialogIcon(title, content)
        dlg.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()