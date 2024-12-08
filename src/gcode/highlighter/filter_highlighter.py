import re

from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor



class QCodeFilterHighlighter(QSyntaxHighlighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_text = ""

    def highlightBlock(self, text):
        if not self.search_text:
            return

        text_char_format = QTextCharFormat()
        text_char_format.setBackground(QColor("#FF6B00"))

        for match in re.finditer(
                re.escape(self.search_text), text, re.IGNORECASE):
            start = match.start()
            length = match.end() - start
            self.setFormat(start, length, text_char_format)


    def filter_text(self, text: str) -> None:
        """Highlighting the searched text

        Args:
            text
                search text
        """
        self.search_text = text
        self.rehighlight()
