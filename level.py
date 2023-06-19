import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QGridLayout


class LevelWindow(QWidget):
    def __init__(self, input_file, menu_window):
        super().__init__()
        self.setWindowTitle('Уровень')
        self.menu_window = menu_window
        self.input_file = input_file
        self.level = self.get_level_from_filename()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.create_title_label()
        self.create_buttons_layout()
        self.create_buttons()
        self.create_exit_and_restart()

    def get_level_from_filename(self):
        # Получаем номер уровня из имени файла
        filename = self.input_file.split('/')[-1]  # Получаем только имя файла из пути
        level = filename.replace('input', '').replace('.txt', '')
        return level

    def create_title_label(self):
        # QLabel с номером уровня
        title_label = QLabel(f"Уровень {self.level}")
        self.layout.addWidget(title_label, alignment=Qt.AlignCenter)

    def create_buttons_layout(self):
        # Создаем сеточную разметку для кнопок
        self.buttons_layout = QGridLayout()
        self.layout.addLayout(self.buttons_layout)

    def create_buttons(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        self.buttons = []

        for row_idx, row in enumerate(lines):
            row = row.split(' ')
            button_row = []
            for col_idx, char in enumerate(row):
                button = QPushButton()
                button.setFixedSize(30, 30)

                if char == '0':
                    button.setStyleSheet('background-color: rgb(34, 92, 186);')
                elif char == '1':
                    button.setStyleSheet('background-color: rgb(227, 219, 64);')

                button.clicked.connect(self.button_clicked)
                button_row.append(button)
                self.buttons_layout.addWidget(button, row_idx, col_idx)

            self.buttons.append(button_row)

        self.layout.addStretch()

    #;lsfkg;sdlfjg
    def create_exit_and_restart(self):
        reload_button = QPushButton('Перезагрузить')
        reload_button.clicked.connect(self.reload_level)
        self.layout.addWidget(reload_button, alignment=Qt.AlignCenter)

        # Кнопка выхода
        exit_button = QPushButton('Выход')
        exit_button.clicked.connect(self.exit_game)
        self.layout.addWidget(exit_button, alignment=Qt.AlignCenter)

    def button_clicked(self):
        clicked_button = self.sender()
        row, col = self.get_button_position(clicked_button)

        # Меняем значение кнопки на противоположное
        if clicked_button.styleSheet() == 'background-color: rgb(34, 92, 186);':
            clicked_button.setStyleSheet('background-color: rgb(227, 219, 64);')
        else:
            clicked_button.setStyleSheet('background-color: rgb(34, 92, 186);')

        # Меняем цвет у соседних кнопок
        self.change_neighbour_buttons_color(row, col)

        # Проверяем, все ли значения кнопок равны 0
        if self.check_win_condition():
            self.show_win_message()

    def get_button_position(self, button):
        for row_idx, row in enumerate(self.buttons):
            if button in row:
                col_idx = row.index(button)
                return row_idx, col_idx

    def change_neighbour_buttons_color(self, row, col):
        # Меняем цвет у соседних кнопок
        neighbour_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for r, c in neighbour_positions:
            if 0 <= r < len(self.buttons) and 0 <= c < len(self.buttons[r]):
                button = self.buttons[r][c]
                if button.styleSheet() == 'background-color: rgb(34, 92, 186);':
                    button.setStyleSheet('background-color: rgb(227, 219, 64);')
                else:
                    button.setStyleSheet('background-color: rgb(34, 92, 186);')

    def check_win_condition(self):
        # Проверяем, все ли значения кнопок равны 0
        for row in self.buttons:
            for button in row:
                if button.styleSheet() == 'background-color: rgb(227, 219, 64);':
                    return False
        return True

    def show_win_message(self):
        # Выводим сообщение о победе
        QMessageBox.information(self, 'Победа!', 'Вы победили!')

    def reload_level(self):
        # Перезагрузка уровня
        self.buttons_layout.removeWidget(self.buttons[0][0])
        for row in self.buttons:
            for button in row:
                self.buttons_layout.removeWidget(button)
                button.deleteLater()

        self.create_buttons()

    def exit_game(self):
        # Закрытие окна уровня и открытие окна меню
        self.close()
        self.menu_window.show()


if __name__ == '__main__':
    app = QApplication([])
    menu_window = QWidget()
    menu_window.show()
    input_file = 'input.txt'
    level_window = LevelWindow(input_file, menu_window)
    level_window.show()
    app.exec_()



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     menu_window = QWidget()
#     menu_window.setWindowTitle('Меню')
#     menu_layout = QVBoxLayout()
#
#     label = QLabel('Lights Out')
#     menu_layout.addWidget(label, alignment=Qt.AlignCenter)
#
#     level_button = QPushButton('Уровень')
#     level_button.clicked.connect(lambda: show_level_window('input.txt'))
#     menu_layout.addWidget(level_button, alignment=Qt.AlignCenter)
#
#     exit_button = QPushButton('Выход')
#     exit_button.clicked.connect(app.quit)
#     menu_layout.addWidget(exit_button, alignment=Qt.AlignCenter)
#
#     menu_window.setLayout(menu_layout)
#     menu_window.show()
#
#     level_window = None
#
#     def show_level_window(input_file):
#         nonlocal level_window
#         if level_window is not None:
#             level_window.close()
#         level_window = LevelWindow(input_file)
#         level_window.show()
#
#     sys.exit(app.exec_())
