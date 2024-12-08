from PySide6.QtWidgets import QWidget, QVBoxLayout, QFileDialog
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

        self.setStyleSheet("""
            #gcode_text_edit_line_number { 
                background-color: #D9D9D9; 
            }
        """)

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
