from PyQt5 import QtCore
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget
from widgets import ui_parameters

class StringInput(QWidget):

    string_recieved_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.root_layout = QHBoxLayout(self)
        self.text_input = QLineEdit()
        self.confirm_button = QPushButton('+')
        self.root_layout.addWidget(self.text_input)
        self.root_layout.addWidget(self.confirm_button)
        self.confirm_button.clicked.connect(self._on_confirm)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.confirm_button.setFixedSize(*ui_parameters.pluss_button_size)
        self.text_input.setFixedHeight(ui_parameters.pluss_button_size[1]-2)
        self.root_layout.setContentsMargins(0, 0, 0, 0)

    def _on_confirm(self):
        self.string_recieved_signal.emit(self.text_input.text())
        self.text_input.setText('')
