from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QObject, pyqtSignal
from widgets.string_input import StringInput

from widgets.toggleable_button import ToggleableButton

class ButtonSelect(QWidget):

    selection_signal = pyqtSignal(object)

    def __init__(self, labels=None):
        QWidget.__init__(self)
        labels = [] if labels is None else labels

        self.selected = None

        self.root_layout = QHBoxLayout(self)
        self.button_layout = QVBoxLayout()
        self.root_layout.addLayout(self.button_layout)
        self.buttons = {label: ToggleableButton(label) for label in labels}
        for label, button in self.buttons.items():
            button.is_down_signal.connect(lambda is_down, label=label : self._on_input(label, is_down))
            self.button_layout.addWidget(button)

        self.root_layout.setContentsMargins(0, 0, 0, 0)

    def _on_input(self, label, is_down):
        if self.selected:
            self.buttons[self.selected].reset()
        selected = label if is_down else None
        self._change_selection(selected)

    def _change_selection(self, selected):
        self.selected = selected
        self.selection_signal.emit([self.selected])

    def _deselect(self):
        if self.selected:
            self._on_input(self.selected, False)


class AppendableButtonSelect(ButtonSelect):

    def __init__(self, labels=None):
        super().__init__(labels)
        self.string_input = StringInput(button_label='+')
        self.string_input.string_recieved_signal.connect(self._add_option)
        self.button_layout.addWidget(self.string_input)


    def _add_option(self, label):
        if label.strip(' ') != '':
            self.buttons[label] = ToggleableButton(label)
            self.buttons[label].is_down_signal.connect(lambda is_down, label=label : self._on_input(label, is_down))
            self.button_layout.insertWidget(len(self.buttons)-1, self.buttons[label])


class TreeSelect(AppendableButtonSelect):

    def __init__(self, tree={}):
        self.tree = {}
        for label, branch in tree.items():
            self.tree[label] = TreeSelect(branch)
            self.tree[label].selection_signal.connect(self._on_next_selection_signal)
        super().__init__(self.tree.keys())

    def _add_option(self, label):
        super()._add_option(label)
        self.tree[label] = TreeSelect()
        self.tree[label].selection_signal.connect(self._on_next_selection_signal)
        
    def _change_selection(self, selection):
        self._close_next()
        super()._change_selection(selection)
        if self.selected:
            self.root_layout.addWidget(self.tree[self.selected])
        
    def _close_next(self):
        if self.selected:
            self.tree[self.selected]._close_next()
            self.tree[self.selected]._deselect()
            self.tree[self.selected].setParent(None)

    def _on_next_selection_signal(self, label):
        self.selection_signal.emit([self.selected] + label)
