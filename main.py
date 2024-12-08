from PySide6.QtWidgets import QApplication

from gcode import GCodeWidget


def main():
    app = QApplication([])
    window = GCodeWidget()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()