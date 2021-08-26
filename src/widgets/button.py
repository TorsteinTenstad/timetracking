from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal

class Button(QPushButton):

    clicked_signal = pyqtSignal()

    def __init__(self, label='Button', size=None, size_policy=None, style_sheet=None, start_enabled=True):
        super().__init__(label)
        if size:
            self.setFixedSize(*size)
        if size_policy:
            self.setSizePolicy(size_policy)
        if style_sheet:
            self.setStyleSheet(style_sheet)
        self.setEnabled(start_enabled)
        self.clicked.connect(self.on_clicked)

    def on_clicked(self, checked):
        self.clicked_signal.emit()
