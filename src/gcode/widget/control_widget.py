from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ABCPushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(QSize(43, 43))
        self.setCheckable(True)


class GCodeControlWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground)

        self.setObjectName('gcode_widget_control')

        self.open_file_button = QPushButton('Open File')
        self.open_file_button.clicked.connect(self.action_open_file)
        self.open_file_button.setObjectName('gcode_button_open_file')
        self.open_file_button.setIcon(QIcon('src/gcode/icon/folder.svg'))
        self.open_file_button.setFixedSize(QSize(422, 43))
        self.open_file_button.setIconSize(QSize(20, 15))

        self.drive_button = ABCPushButton()
        self.drive_button.clicked.connect(self.action_drive_button)
        self.drive_button.setObjectName('gcode_button_drive')

        self.filter_button = ABCPushButton()
        self.filter_button.clicked.connect(self.action_filter_button)
        self.filter_button.setObjectName('gcode_button_filter')

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.open_file_button)
        self.layout.addWidget(self.drive_button)
        self.layout.addWidget(self.filter_button)

        self.layout.setContentsMargins(0, 3, 0, 3)
        self.layout.setSpacing(0)

    def action_drive_button(self):
        """Action hidden GCodeFilterWidget"""
        self.parent().hidden_filter_widget()
        self.drive_button.setChecked(True)
        self.filter_button.setChecked(False)

    def action_filter_button(self):
        """Action show GCodeFilterWidget"""
        self.parent().show_filter_widget()
        self.drive_button.setChecked(False)
        self.filter_button.setChecked(True)

    def action_open_file(self):
        self.parent().open_file()

    def set_file_name(self, file_name: str) -> None:
        self.open_file_button.setText(file_name)
