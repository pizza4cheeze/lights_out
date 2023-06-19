import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from level import LevelWindow
from instruction import InstructionWindow


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lights Out')
        self.layout = QVBoxLayout()

        # Label с названием игры
        self.label = QLabel('Lights Out')
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Кнопки уровней
        for level in range(1, 6):
            level_button = QPushButton(f'Уровень {level}')
            level_button.clicked.connect(lambda _, lvl=level: self.start_level(lvl))
            self.layout.addWidget(level_button)

        # Кнопка выхода
        exit_button = QPushButton('Выход')
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button)

        instruction_button = QPushButton('Инструкция')
        instruction_button.clicked.connect(self.open_instructions)
        self.layout.addWidget(instruction_button)

        self.setLayout(self.layout)

    def start_level(self, level):
        file_name = f"inputs/input{level}.txt"
        self.level_window = LevelWindow(file_name, self)  # Сохраняем ссылку на объект LevelWindow
        self.level_window.show()
        return self.level_window

    def open_instructions(self):
        self.instruction_window = InstructionWindow(self)
        self.instruction_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(app.exec_())
