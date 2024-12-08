from PySide6 import QtGui
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout


class GCodeFilterWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground)

        self.setObjectName('gcode_widget_filter')
        self.setContentsMargins(0, 0, 0, 0)

        self.filter_line_edit = QLineEdit()
        self.filter_line_edit.textChanged.connect(self.action_filter_text)
        self.filter_line_edit.setObjectName('gcode_filter_line_edit')
        self.filter_line_edit.setFixedSize(155, 20)

        self.filter_label_search = QLabel('Найти')
        self.filter_label_search.setObjectName('gcode_filter_label_search')

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.filter_label_search)
        self.layout.addWidget(self.filter_line_edit)
        self.layout.setContentsMargins(10, 5, 2, 7)
        self.layout.setSpacing(0)

        self.setFixedSize(179, 52)

        radius = 5.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(self.rect(), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def showEvent(self, event):
        super().showEvent(event)
        self.move(self.parent().width() - self.width() - 10, 1)

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
