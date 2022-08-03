from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import playground
import menu
import game_engine
import copy
import resources

matrix = game_engine.Matrix()
grid_size = 4

colors = {
    'label': '#2b2b2b',
    '': '#d8bfd8',
    '2': '#ee82ee',
    '4': '#da70d6',
    '8': '#ff00c0',
    '16': '#bf5fff',
    '32': '#ff1cae',
    '64': '#6030a8',
    '128': '#8b008b',
    '256': '#800080',
    '512': '#4b0082',
    '1024': '#371f76',
    '2048': '#ffa701',
    '4096': '#b81324'
}


class PlayWindow(QMainWindow, playground.Ui_MainWindow):
    def __init__(self):
        # PlayWindow UI setup
        super().__init__()
        self.setupUi(self)

        self.setFixedWidth(400)
        self.setFixedHeight(560)
        self.setWindowIcon(QIcon(':logos/logo64'))

        # PlayWindow widgets styling
        self.button_back.clicked.connect(self.back_to_menu)
        self.label_score.setStyleSheet(f"background-color:{colors['4']};"
                                       f"border-radius: 10;"
                                       f"color: {colors['label']}")
        self.button_back.setStyleSheet(f"background-color:{colors['2']};"
                                       f"border-radius: 10;"
                                       f"color: {colors['label']}")
        self.score.setStyleSheet(f"border-radius: 10;"
                                 f"background-color: rgb(210, 210, 210);"
                                 f"color: {colors['label']}")
        self.setStyleSheet(f"background-color: #1b1b1b")

        # Create Matrix object
        self.matrix = game_engine.Matrix(size=grid_size)
        self.matrix.add_cell()
        self.update_grid()

    def keyPressEvent(self, e):
        flag = False
        if e.key() == Qt.Key_A:
            flag = True
            self.matrix.move_left()
        if e.key() == Qt.Key_D:
            flag = True
            self.matrix.move_right()
        if e.key() == Qt.Key_S:
            flag = True
            self.matrix.move_down()
        if e.key() == Qt.Key_W:
            flag = True
            self.matrix.move_up()

        # if the matrix was changed update the grid
        if self.matrix.data != self.matrix.prev_data:
            self.matrix.prev_data = copy.deepcopy(self.matrix.data)
            self.matrix.add_cell()
            self.update_grid()

        # Check game status
        if self.matrix.is_won():
            self.label_score.setStyleSheet(f"background-color: #ffe338;"
                                           f"border-radius: 10;"
                                           f"color: {colors['4']}")
            self.label_score.setText('YOU WON!!!')
        if self.matrix.is_gameover():
            self.label_score.setStyleSheet(f"background-color: red;"
                                           f"border-radius: 10;"
                                           f"color: black")
            self.label_score.setText('GAME OVER')

    def update_grid(self):
        for i in range(len(self.matrix.data)):
            for j in range(len(self.matrix.data)):
                value = self.matrix.data[i][j]
                value = str(value) if str(value) != '0' else ''
                
                current_label = QLabel(value)
                current_label.setAlignment(Qt.AlignCenter)

                color = colors.get(current_label.text(), colors['4096'])

                current_label.setStyleSheet("border: 2px solid black;"
                                            "border-radius: 10;"
                                            f"background-color: {color};"
                                            "color: rgb(10, 10, 10)")
                current_label.setFont(QFont('Arial', 100 // grid_size))
                self.data_grid.addWidget(current_label, i, j)
        self.score.setText(str(self.matrix.score))

    def back_to_menu(self):
        menu_page = StartWindow()
        widget.addWidget(menu_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class StartWindow(QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        # PlayWindow UI setup
        super().__init__()
        self.setupUi(self)

        self.setFixedWidth(400)
        self.setFixedHeight(560)

        # PlayWindow widgets styling
        self.setStyleSheet(f"background-color: #1b1b1b")
        self.button_play.clicked.connect(self.start_the_game)
        self.button_play.setStyleSheet(f"background-color: {colors['4']};"
                                       f"color: white;"
                                       f"border-radius: 10;")
        self.grid_size.setStyleSheet(f"background-color: #ffffff;"
                                     f"color: {colors['4']}")

    def start_the_game(self):
        global grid_size
        grid_size = int(self.grid_size.text())
        play_ground = PlayWindow()
        widget.addWidget(play_ground)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication([])
app.setWindowIcon(QIcon(':/logos/logo64'))
app.setApplicationName('2048')

start_page = StartWindow()

widget = QStackedWidget()
widget.addWidget(start_page)
widget.setFixedWidth(400)
widget.setFixedHeight(560)
widget.setWindowTitle('2048')

widget.show()

app.exec()
