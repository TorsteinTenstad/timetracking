from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget

from widgets import ui_parameters

class StartStopButtons(QWidget):

    start_signal = pyqtSignal()
    stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

        self.button_layout = QHBoxLayout(self)

        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stop')

        for button in [self.start_button, self.stop_button]:
            self.button_layout.addWidget(button)
            button.clicked.connect(self._on_input)
            button.setStyleSheet(ui_parameters.large_text)
            button.setFixedSize(*ui_parameters.large_button_size)
        self.setEnabled(False)

    def _on_input(self):
        self.running = not self.running
        self.start_button.setEnabled(not self.running)
        self.stop_button.setEnabled(self.running)
        if self.running:
            self.start_signal.emit()
        else:
            self.stop_signal.emit()

    def setEnabled(self, enabled):
        if enabled:
            self.start_button.setEnabled(not self.running)
            self.stop_button.setEnabled(self.running)
        else:
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(False)
