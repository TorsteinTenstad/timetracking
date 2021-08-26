from PyQt5 import QtCore
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget

class StringInput(QWidget):

    string_recieved_signal = pyqtSignal(str)

    def __init__(self, button_label):
        super().__init__()
        self.root_layout = QHBoxLayout(self)
        self.text_input = QLineEdit()
        self.confirm_button = QPushButton(button_label)
        self.root_layout.addWidget(self.text_input)
        self.root_layout.addWidget(self.confirm_button)
        self.confirm_button.clicked.connect(self._on_confirm)

        #self.text_input.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        #self.confirm_button.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))
        #self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.root_layout.setContentsMargins(0, 0, 0, 0)

    def _on_confirm(self):
        self.string_recieved_signal.emit(self.text_input.text())
        self.text_input.setText('')
