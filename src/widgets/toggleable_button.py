from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal
from widgets import ui_parameters

class ToggleableButton(QPushButton):

    is_down_signal = pyqtSignal(bool)

    def __init__(self, label='Button'):
        super().__init__(label)
        self.setCheckable(True)
        self.clicked.connect(self._on_clicked)
        self.setStyleSheet(ui_parameters.global_stylesheet)
        self.setFixedSize(*ui_parameters.regular_long_button_size)

    def _on_clicked(self):
        self.is_down_signal.emit(self.isChecked())

    def reset(self):
        self.setChecked(False)
