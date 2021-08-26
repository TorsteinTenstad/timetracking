# Button sizes:
large_button_size = (80*1.618, 80)
regular_long_button_size = (256, 30)
pluss_button_size = (30, 30)


# Stylesheets:
regular_text = 'font-size: 12pt'
large_text = 'font-size: 18pt'
huge_text = 'font-size: 22pt'

global_stylesheet = '''
QPushButton {
    font-size: 13pt;
}
QPushButton:checked {
    font-size: 13pt;
    border:  1px solid rgba(160, 169, 175, 255); 
    color: black;
    background-color: rgba(50, 140, 200, 255);
}
QPushButton:disabled {
    font-size: 13pt;
}'''
