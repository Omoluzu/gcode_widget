from PySide6.QtWidgets import QWidget



class GCodeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('GCode - Тестовое задание Волков Алексей Сергеевич')