import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QWidget
from widgets.button import Button
from widgets.button_select import TreeSelect
from widgets.start_stop_buttons import StartStopButtons
from widgets.string_input import StringInput
from widgets.toggleable_button import ToggleableButton



categories = ['Studier;Prosjektoppgave',
                'Studier;Språk',
                'Studier;Medisinsk DSP',
                'Studier;Taleteknologi',
                'Jobb']


app = QApplication(sys.argv)

widget = TreeSelect()
widget.selection_signal.connect(lambda x : print(x))

root_widget = QWidget()
root_layout = QVBoxLayout(root_widget)
root_layout.addWidget(widget)
window = QMainWindow()
window.setCentralWidget(root_widget)
window.show()

sys.exit(app.exec_())
