from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout


class GCodeShowBlockCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.number_line_text_edit = QTextEdit()
        self.code_text_edit = QTextEdit()

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.number_line_text_edit)
        self.layout.addWidget(self.code_text_edit)
