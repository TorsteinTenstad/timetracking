
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from widgets.button_select import TreeSelect
from widgets.start_stop_buttons import StartStopButtons

class UI(QMainWindow):

    start_signal = pyqtSignal()
    stop_signal = pyqtSignal()
    category_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def init_ui(self, categories_tree):
        self.root_widget = QWidget()
        self.root_layout = QHBoxLayout(self.root_widget)

        self.timer_panel = StartStopButtons()
        self.timer_panel.start_signal.connect(lambda : self.start_signal.emit())
        self.timer_panel.stop_signal.connect(lambda : self.stop_signal.emit())
        self.root_layout.addWidget(self.timer_panel, alignment=QtCore.Qt.AlignTop)
        self.category_selector = TreeSelect(categories_tree)
        self.category_selector.selection_signal.connect(lambda category : self.category_signal.emit(';'.join(category)))
        self.root_layout.addWidget(self.category_selector, alignment=QtCore.Qt.AlignTop)

        self.setCentralWidget(self.root_widget)
        self.setWindowTitle('Timetracker')
        self.show()