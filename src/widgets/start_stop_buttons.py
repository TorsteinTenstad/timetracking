from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from widgets import ui_parameters

class StartStopButtons(QWidget):

    start_signal = pyqtSignal()
    stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.button_layout = QHBoxLayout(self)

        self.start_button = QPushButton('Start')
        self.button_layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self._on_start)
        self.start_button.setStyleSheet(ui_parameters.large_text)
        self.start_button.setFixedSize(*ui_parameters.large_button_size)

        self.stop_button = QPushButton('Stop')
        self.button_layout.addWidget(self.stop_button)
        self.stop_button.clicked.connect(self._on_stop)
        self.stop_button.setStyleSheet(ui_parameters.large_text)
        self.stop_button.setFixedSize(*ui_parameters.large_button_size)
        self.stop_button.setEnabled(False)

    def _on_start(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.start_signal.emit()

    def _on_stop(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.stop_signal.emit()