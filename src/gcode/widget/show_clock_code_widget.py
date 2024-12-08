from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QStackedLayout

from gcode import widget, text_edit, highlighter



class GCodeShowBlockCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.number_line_text_edit = text_edit.GCodeNumberLine()
        self.code_text_edit = QTextEdit()
        self.filter_widget = widget.GCodeFilter()

        self.highlighter = highlighter.GCodeFilter(
            self.code_text_edit.document())

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.setStackingMode(QStackedLayout.StackAll)
        self.stacked_layout.addWidget(self.code_text_edit)
        self.stacked_layout.addWidget(self.filter_widget)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.number_line_text_edit)
        self.layout.addLayout(self.stacked_layout)

        self.set_logical_vertical_scroll_bar()

    def set_logical_vertical_scroll_bar(self) -> None:
        """Set logical vertical scroll bar"""
        self.number_line_text_edit.verticalScrollBar().valueChanged.connect(
            self.code_text_edit.verticalScrollBar().setValue)

        self.code_text_edit.verticalScrollBar().valueChanged.connect(
            self.number_line_text_edit.verticalScrollBar().setValue)

    def hidden_filter_widget(self) -> None:
        """Hidden GCodeFilterWidget"""
        self.filter_widget.hidden_filter_widget()

    def show_filter_widget(self) -> None:
        """Show GCodeFilterWidget"""
        self.filter_widget.setVisible(True)

    def content_output(self, file_content: list[str]) -> None:
        """Outputting content to text widgets

        Args:
            file_content:
                File contents
        """
        self.code_text_edit.setPlainText(''.join(file_content))
        self.number_line_text_edit.setPlainText(
            '\n'.join(map(str, (range(1, len(file_content) + 1)))))

    def filter_text(self, text: str) -> None:
        """Search text and highlight its text

        Args:
            text
                Search text
        """
        self.highlighter.filter_text(text)

