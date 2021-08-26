import sys
import time
from PyQt5 import QtWidgets
from time_logger import TimeLogger
from ui import UI


def create_dict_tree(path_strings):
    tree = {}
    for path_string in path_strings:
        path = path_string.split(';')
        current_branch = tree
        for x in path:
            if x in tree.keys():
                current_branch = current_branch[x]
            else:
                current_branch[x] = {}
                current_branch = current_branch[x]
    return tree


def main():
    app = QtWidgets.QApplication(sys.argv)

    ui = UI()
    time_logger = TimeLogger('time_log.csv')

    categories_tree = create_dict_tree(time_logger.get_categories())
    ui.init_ui(categories_tree)

    ui.start_signal.connect(time_logger.start_session)
    ui.stop_signal.connect(time_logger.stop_session)
    ui.category_signal.connect(time_logger.set_category)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()