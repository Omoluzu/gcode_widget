import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog
from PySide6.QtCore import QSize

from gcode import widget, style



class GCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName('gcode_main')

        self.setWindowTitle('GCode - Тестовое задание Волков Алексей Сергеевич')
        self.setFixedSize(QSize(528, 346))

        self.control_widget = widget.GCodeControl()
        self.show_block_code_widget = widget.GCodeShowBlockCode()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.control_widget)
        self.layout.addWidget(self.show_block_code_widget)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setStyleSheet(style.gcode.style)

        self.control_widget.action_drive_button()

    def hidden_filter_widget(self) -> None:
        """Hidden GCodeFilterWidget"""
        self.show_block_code_widget.hidden_filter_widget()

    def show_filter_widget(self) -> None:
        """Show GCodeFilterWidget"""
        self.show_block_code_widget.show_filter_widget()

    def filter_text(self, text: str) -> None:
        """Search text and highlight its text

        Args:
            text
                Search text
        """
        self.show_block_code_widget.filter_text(text)

    def open_file(self) -> None:
        """Open GCode file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "GCodeFile (*.txt)")

        if filename:
            with open(filename, encoding='utf-8') as file:
                self.show_block_code_widget.content_output(
                    file_content=file.readlines())

            self.control_widget.set_file_name(
                file_name=os.path.basename(filename))
