from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout


class GCodeFilterWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel('Найти'))
        self.layout.addWidget(QLineEdit())

        self.setFixedSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 128))

    def showEvent(self, event):
        super().showEvent(event)
        self.move(self.parent().width() - self.width(), 0)
