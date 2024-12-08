from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout


class GCodeFilterWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filter_line_edit = QLineEdit()
        self.filter_line_edit.textChanged.connect(self.action_filter_text)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel('Найти'))
        self.layout.addWidget(self.filter_line_edit)

        self.setFixedSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 128))

    def showEvent(self, event):
        super().showEvent(event)
        self.move(self.parent().width() - self.width(), 0)

    def action_filter_text(self, text: str) -> None:
        """Activate text highlighting

        Args:
            text
                Search text
        """
        self.parent().filter_text(text)

    def hidden_filter_widget(self):
        """Hidden GCodeFilterWidget"""
        self.setVisible(False)
        self.filter_line_edit.setText('')
