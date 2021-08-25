import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QWidget
from widgets.button_select import TreeSelect
from widgets.string_input import StringInput
from widgets.toggleable_button import ToggleableButton


app = QApplication(sys.argv)

tree = {'A' : {'A1': {'A1.1': {}}, 'A2': {}}, 'B': {}}

widget = TreeSelect(tree)
widget.selection_signal.connect(lambda x : print(x))

window = QMainWindow()
window.setCentralWidget(widget)
window.show()

sys.exit(app.exec_())
