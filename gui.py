import sys
import main
from PyQt5 import QtWidgets, QtGui, QtCore


class SimpleChatApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чат")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #eaeaea;")

        # Создание интерфейса
        self.create_widgets()

        self.conf = main.get_api_keys('api.ini')
        self.DeepSeek = main.AIConsultant(self.conf['DeepSeek'])
        self.GG = main.AIConsultant(self.conf['Google Gemini'])
        self.GPT = main.AIConsultant(self.conf['Chat GPT'])

    def create_widgets(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Выпадающий список
        self.service_combobox = QtWidgets.QComboBox()
        self.service_combobox.addItems(["DeepSeek", "Google Gemini", "Chat GPT"])
        self.service_combobox.setStyleSheet("""
            QComboBox {
                padding: 10px;
                font-size: 14px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.service_combobox)

        # Поле для отображения сообщений
        self.chat_history = QtWidgets.QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setFont(QtGui.QFont('Segoe UI', 11))
        self.chat_history.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.chat_history)

        # Поле ввода сообщения
        self.user_input = QtWidgets.QTextEdit()
        self.user_input.setFixedHeight(50)
        self.user_input.setFont(QtGui.QFont('Segoe UI', 11))
        self.user_input.setPlaceholderText("Введите ваше сообщение...")
        self.user_input.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                background-color: #fff;
            }
        """)
        layout.addWidget(self.user_input)

        # Кнопка отправки
        send_button = QtWidgets.QPushButton("Отправить")
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        # Установка отступов
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

    def send_message(self):
        user_text = self.user_input.toPlainText().strip()

        if not user_text:
            QtWidgets.QMessageBox.warning(self, "Пустое сообщение", "Пожалуйста, введите ваше сообщение.")
            return

        # Отображение сообщения пользователя
        self.chat_history.append(f"<b>Вы:</b> {user_text}")
        self.user_input.clear()
        if self.service_combobox.currentText() == 'Google Gemini':
            self.chat_history.append(f"<b>Ответ:</b> {self.GG.get_ai_response(user_text)}")
        if self.service_combobox.currentText() == 'DeepSeek':
            self.chat_history.append(f"<b>Ответ:</b> {self.DeepSeek.get_ai_response(user_text)}")
        if self.service_combobox.currentText() == 'Chat GPT':
            self.chat_history.append(f"<b>Ответ:</b> {self.GPT.get_ai_response(user_text)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SimpleChatApp()
    window.show()
    sys.exit(app.exec_())