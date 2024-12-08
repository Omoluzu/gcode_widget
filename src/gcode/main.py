from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QSize

from gcode import widget



class GCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('GCode - Тестовое задание Волков Алексей Сергеевич')
        self.setFixedSize(QSize(528, 346))

        self.control_widget = widget.GCodeControl()
        self.show_block_code_widget = widget.GCodeShowBlockCode()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.control_widget)
        self.layout.addWidget(self.show_block_code_widget)

        self.hidden_filter_widget()

    def hidden_filter_widget(self):
        """Hidden GCodeFilterWidget"""
        self.show_block_code_widget.hidden_filter_widget()

    def show_filter_widget(self):
        """Show GCodeFilterWidget"""
        self.show_block_code_widget.show_filter_widget()
