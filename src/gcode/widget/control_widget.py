from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class GCodeControlWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.select_file_button = QPushButton('Open File')
        self.drive_button = QPushButton('Drive')
        self.filter_button = QPushButton('Filter')

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.select_file_button)
        self.layout.addWidget(self.drive_button)
        self.layout.addWidget(self.filter_button)
