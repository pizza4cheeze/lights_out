from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication


class InstructionWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Инструкция")
        self.setGeometry(100, 100, 400, 300)
        self.main_window = main_window

        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel("Правила игры", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label, alignment=Qt.AlignLeft | Qt.AlignTop)

        text_label = QLabel("Текст", self)
        text_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(text_label, alignment=Qt.AlignLeft)

        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = InstructionWindow()
    sys.exit(app.exec_())

