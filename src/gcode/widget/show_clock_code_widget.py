from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QStackedLayout

from gcode import widget



class GCodeShowBlockCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.number_line_text_edit = QTextEdit()
        self.code_text_edit = QTextEdit()
        self.filter_widget = widget.GCodeFilter()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.setStackingMode(QStackedLayout.StackAll)
        self.stacked_layout.addWidget(self.code_text_edit)
        self.stacked_layout.addWidget(self.filter_widget)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.number_line_text_edit)
        self.layout.addLayout(self.stacked_layout)

    def hidden_filter_widget(self):
        """Hidden GCodeFilterWidget"""
        self.filter_widget.setVisible(False)

    def show_filter_widget(self):
        """Show GCodeFilterWidget"""
        self.filter_widget.setVisible(True)
