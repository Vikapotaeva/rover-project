import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel)
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QVBoxLayout()
central_widget.setLayout(layout)
text_input = QTextEdit()
text_input.setPlaceholderText("Введите ваш текст здесь")
layout.addWidget(text_input)
process_button = QPushButton("Анализ текста")
layout.addWidget(process_button)
result_output = QTextEdit()
result_output.setReadOnly(True)  #Только для чтения
result_output.setPlaceholderText("Здесь появится результат")
layout.addWidget(result_output)

def on_button_click():
    input_text = text_input.toPlainText()
    char_count = len(input_text)
    result_text = f'количество символов: {char_count}'
    result_output.setPlainText(result_text)
process_button.clicked.connect(on_button_click)

window.show()
sys.exit(app.exec())