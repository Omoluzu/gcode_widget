from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QTextEdit


class GCodeNumberLineTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignRight)
        self.setFixedSize(QSize(43, 289))

        self.setObjectName('gcode_text_edit_line_number')