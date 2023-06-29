import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 300, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.create_buttons()

    def create_buttons(self):
        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, button in zip(positions, self.buttons):
            push_button = QPushButton(button)
            push_button.clicked.connect(self.button_clicked)
            self.grid_layout.addWidget(push_button, *position)

    def button_clicked(self):
        button = self.sender()
        text = button.text()
        current_display = self.result_display.text()

        if text == '=':
            try:
                result = eval(current_display)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        else:
            self.result_display.setText(current_display + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
