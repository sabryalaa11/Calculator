import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                            QPushButton, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Calculator")
        self.setFixedSize(400, 600)
        
        # Set the color scheme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QLineEdit {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 2px solid #3D3D3D;
                border-radius: 10px;
                padding: 15px;
                font-size: 28px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #3D3D3D;
                color: #FFFFFF;
                border: none;
                border-radius: 10px;
                padding: 20px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
            QPushButton:pressed {
                background-color: #2D2D2D;
            }
            QPushButton#operator {
                background-color: #FF9500;
                color: #FFFFFF;
            }
            QPushButton#operator:hover {
                background-color: #FFA533;
            }
            QPushButton#operator:pressed {
                background-color: #CC7700;
            }
            QPushButton#equals {
                background-color: #2196F3;
                color: #FFFFFF;
            }
            QPushButton#equals:hover {
                background-color: #42A5F5;
            }
            QPushButton#equals:pressed {
                background-color: #1976D2;
            }
            QPushButton#clear {
                background-color: #F44336;
                color: #FFFFFF;
            }
            QPushButton#clear:hover {
                background-color: #EF5350;
            }
            QPushButton#clear:pressed {
                background-color: #D32F2F;
            }
        """)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        # Create display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(80)
        layout.addWidget(self.display, 0, 0, 1, 4)

        # Button texts
        buttons = {
            (1, 0): '7', (1, 1): '8', (1, 2): '9', (1, 3): '/',
            (2, 0): '4', (2, 1): '5', (2, 2): '6', (2, 3): '*',
            (3, 0): '1', (3, 1): '2', (3, 2): '3', (3, 3): '-',
            (4, 0): '0', (4, 1): '.', (4, 2): '=', (4, 3): '+',
            (5, 0): 'C', (5, 1): 'CE', (5, 2): '(', (5, 3): ')'
        }

        # Create and add buttons
        for (row, col), text in buttons.items():
            button = QPushButton(text)
            button.setFixedSize(85, 85)
            
            if text in ['+', '-', '*', '/']:
                button.setObjectName("operator")
            elif text == '=':
                button.setObjectName("equals")
            elif text in ['C', 'CE']:
                button.setObjectName("clear")
            
            button.clicked.connect(self.button_clicked)
            layout.addWidget(button, row, col)

        self.current_expression = ""

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.current_expression)
                self.display.setText(str(result))
                self.current_expression = str(result)
            except:
                self.display.setText("Error")
                self.current_expression = ""
        elif text == 'C':
            self.current_expression = ""
            self.display.setText("")
        elif text == 'CE':
            self.current_expression = self.current_expression[:-1]
            self.display.setText(self.current_expression)
        else:
            self.current_expression += text
            self.display.setText(self.current_expression)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec()) 