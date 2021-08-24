from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal


class ToggleableButton(QPushButton):

    is_down_signal = pyqtSignal(bool)

    def __init__(self, label='Button'):
        super().__init__(label)
        self.setCheckable(True)
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self):
        self.is_down_signal.emit(self.isChecked())

    def reset(self):
        self.setChecked(False)
