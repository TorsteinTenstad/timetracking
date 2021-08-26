
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from widgets.button_select import TreeSelect
from widgets.start_stop_buttons import StartStopButtons

class UI(QMainWindow):

    start_signal = pyqtSignal(str)
    stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def init_ui(self, categories_tree):
        self.root_widget = QWidget()
        self.root_layout = QHBoxLayout(self.root_widget)

        self.timer_panel = StartStopButtons()
        self.timer_panel.start_signal.connect(self._on_timer_start)
        self.timer_panel.stop_signal.connect(self._on_timer_stop)
        self.root_layout.addWidget(self.timer_panel, alignment=QtCore.Qt.AlignTop)
        self.category_selector = TreeSelect(categories_tree)
        self.category_selector.selection_signal.connect(self._on_category_select)
        self.root_layout.addWidget(self.category_selector, alignment=QtCore.Qt.AlignTop)

        self.setCentralWidget(self.root_widget)
        self.setWindowTitle('Timetracker')
        self.show()
    
    def _on_timer_start(self):
        self.start_signal.emit(self.category)
        self.category_selector.setEnabled(False)

    def _on_timer_stop(self):
        self.stop_signal.emit()
        self.category_selector.setEnabled(True)

    def _on_category_select(self, category):
        if category[0] is None:
            self.timer_panel.setEnabled(False)
        else:
            self.timer_panel.setEnabled(True)
            self.category = ';'.join([x for x in category if x is not None])
        self._resize_to_fit()

    def _resize_to_fit(self):
        self.resize(self.root_widget.minimumSizeHint())