from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class GCodeControlWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.open_file_button = QPushButton('Open File')
        self.open_file_button.clicked.connect(self.action_open_file)

        self.drive_button = QPushButton('Drive')
        self.drive_button.clicked.connect(self.action_drive_button)

        self.filter_button = QPushButton('Filter')
        self.filter_button.clicked.connect(self.action_filter_button)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.open_file_button)
        self.layout.addWidget(self.drive_button)
        self.layout.addWidget(self.filter_button)

    def action_drive_button(self):
        """Action hidden GCodeFilterWidget"""
        self.parent().hidden_filter_widget()

    def action_filter_button(self):
        """Action show GCodeFilterWidget"""
        self.parent().show_filter_widget()

    def action_open_file(self):
        self.parent().open_file()
