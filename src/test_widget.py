import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from widgets.button_select import TreeSelect
from widgets.toggleable_button import ToggleableButton


app = QApplication(sys.argv)

widget = TreeSelect()
widget.selection_signal.connect(lambda x : print(x))

window = QMainWindow()
window.setCentralWidget(widget)
window.show()
sys.exit(app.exec_())
