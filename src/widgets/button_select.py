from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QObject, pyqtSignal
from widgets.string_input import StringInput

from widgets.toggleable_button import ToggleableButton

class ButtonSelect(QWidget):

    selection_signal = pyqtSignal(str)

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

    def _on_input(self, label, is_down):
        if self.selected:
            self.buttons[self.selected].reset()
        self.selected = label if is_down else None
        self.selection_signal.emit(self.selected)

    def deselect(self):
        self._on_input(self.selected, False)


class AppendableButtonSelect(ButtonSelect):

    def __init__(self, labels=None):
        super().__init__(labels)
        self.string_input = StringInput(button_label='Add')
        self.string_input.string_recieved_signal.connect(self.add_option)
        self.button_layout.addWidget(self.string_input)


    def add_option(self, label):
        if label.strip(' ') != '':
            self.buttons[label] = ToggleableButton(label)
            self.buttons[label].is_down_signal.connect(lambda is_down, label=label : self._on_input(label, is_down))
            self.button_layout.insertWidget(len(self.buttons)-1, self.buttons[label])


class TreeSelect(AppendableButtonSelect):

    def __init__(self):
        super().__init__()
        self.tree = {}
        self.next_layer = None
        self.selection_signal.connect(self._on_selected)

    def add_option(self, label):
        super().add_option(label)
        self.tree[label] = TreeSelect()

    def close_next_layer(self):
        if self.next_layer:
            self.next_layer.close_next_layer()
            self.next_layer.deselect()
            self.next_layer.setParent(None)
            self.next_layer = None

    def _on_selected(self, label):
        self.close_next_layer()
        if label:
            self.next_layer = self.tree[label]
            self.root_layout.addWidget(self.next_layer)

