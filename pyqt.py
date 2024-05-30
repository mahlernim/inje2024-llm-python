# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

# app = QApplication([])

# window = QMainWindow()
# window.resize(400, 600)
# window.setWindowTitle("파이썬실습")

# label = QLabel("안녕하세요", alignment=Qt.AlignmentFlag.AlignCenter)
# window.setCentralWidget(label)

# window.show()
# app.exec()

# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget

# def calculate_bmi():
#     height = float(heightInput.text()) / 100
#     weight = float(weightInput.text())
#     bmi = weight / (height ** 2)
#     resultLabel.setText(f"BMI는 {bmi:.2f}입니다.")

# app = QApplication([])

# layout = QVBoxLayout()
# heightInput = QLineEdit("180")
# weightInput = QLineEdit("70")
# calculateButton = QPushButton("Calculate BMI")
# calculateButton.clicked.connect(calculate_bmi)
# resultLabel = QLabel("BMI 계산 결과는?")
# layout.addWidget(heightInput)
# layout.addWidget(weightInput)
# layout.addWidget(calculateButton)
# layout.addWidget(resultLabel)

# widget = QWidget()
# widget.setLayout(layout)

# window = QMainWindow()
# #window.resize(400, 600)
# window.setWindowTitle("파이썬실습")
# window.setCentralWidget(widget)

# window.show()
# app.exec()

# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QDateEdit
# from PyQt6.QtCore import QDate

# def update_days_remaining():
#     today_date = todayDateEdit.date()
#     due_date = dueDateEdit.date()
#     days_remaining = today_date.daysTo(due_date)
#     resultLabel.setText(f" {days_remaining}일 남았습니다.")

# app = QApplication([])
# layout = QGridLayout()
# todayDateEdit = QDateEdit(QDate.currentDate())
# todayDateEdit.setCalendarPopup(True)
# todayDateEdit.dateChanged.connect(update_days_remaining)  # dateChanged 이벤트가 일어나면 함수 실행
# layout.addWidget(QLabel("오늘 날짜:"), 0, 0)  # Top left
# layout.addWidget(todayDateEdit, 1, 0)  # Below the label on the left

# dueDateEdit = QDateEdit(QDate.currentDate().addDays(7))
# dueDateEdit.setCalendarPopup(True)
# dueDateEdit.dateChanged.connect(update_days_remaining)
# layout.addWidget(QLabel("제출 날짜:"), 0, 1)  # Top right
# layout.addWidget(dueDateEdit, 1, 1)  # Below the label on the right

# resultLabel = QLabel("남은 날짜가 표시됩니다.")
# layout.addWidget(resultLabel, 2, 0, 1, 2)  # 2,0 칸에 1줄2열에 걸친 위젯

# widget = QWidget()
# widget.setLayout(layout)

# window = QMainWindow()
# window.setWindowTitle("날짜계산기")
# window.setCentralWidget(widget)
# window.show()
# app.exec()


# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QRadioButton, QWidget, QButtonGroup, QListWidget

# def update_price():
#     size_index = sizeList.currentIndex().row()
#     topping_index = toppingGroup.checkedId()
#     order_type = orderTypeCombo.currentText()
#     size_prices = [2, 1.5, 1]
#     topping_prices = [12000, 14000, 16000]
#     price = int(size_prices[size_index] * topping_prices[topping_index])
#     if order_type == "배달":
#         price += 5000
#     priceLabel.setText(f"총 주문 금액: {price:,}원")

# app = QApplication([])
# layout = QVBoxLayout()

# layout.addWidget(QLabel('사이즈:'))
# sizeList = QListWidget()
# sizeList.addItems(['큰거', '중간', '작은거'])
# sizeList.currentItemChanged.connect(update_price)  # Connect to update function
# layout.addWidget(sizeList)

# layout.addWidget(QLabel('토핑:'))
# toppingGroup = QButtonGroup()
# toppings = ['페퍼로니', '슈프림', '불고기']
# for i, topping in enumerate(toppings):
#     button = QRadioButton(topping)
#     layout.addWidget(button)
#     toppingGroup.addButton(button, i)  # Assign an ID to each button
#     if i == 0:
#         button.setChecked(True)  # Default selection
# toppingGroup.buttonClicked.connect(update_price)  # Connect to update function

# layout.addWidget(QLabel('주문종류:'))
# orderTypeCombo = QComboBox()
# orderTypeCombo.addItems(['배달', '포장'])
# orderTypeCombo.currentIndexChanged.connect(update_price)  # Connect to update function
# layout.addWidget(orderTypeCombo)

# priceLabel = QLabel("총 주문 금액:")
# layout.addWidget(priceLabel)

# widget = QWidget()
# widget.setLayout(layout)
# window = QMainWindow()
# window.setWindowTitle("인제피자")
# window.setCentralWidget(widget)
# window.show()
# app.exec()


from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit

def generate_story():
    import google.generativeai as genai
    genai.configure(api_key="yourapikey")
    model = genai.GenerativeModel('gemini-pro')
    keywords = keyword_input.text()
    style = style_input.currentText()
    prompt = f"""다음 조건을 지켜 3문장 정도의 재미있는 이야기를 지어주세요.
    - 포함할 키워드: {keywords}
    - 이야기의 문체: {style}"""
    response = model.generate_content(prompt)
    story_output.setText(response.text)

app = QApplication([])
layout = QVBoxLayout()

keyword_input = QLineEdit()
keyword_input.setPlaceholderText('키워드를 콤마로 구분')
layout.addWidget(QLabel('키워드:'))
layout.addWidget(keyword_input)

style_input = QComboBox()
styles = [
    "'옛날옛적에'로 시작하는 전래동화",
    "막장 아침 드라마 줄거리",
    "친구한테 들은 인터넷썰 커뮤니티 문체로"
]
style_input.addItems(styles)
layout.addWidget(QLabel('스타일 선택:'))
layout.addWidget(style_input)

generate_button = QPushButton('잼얘 생성!')
layout.addWidget(generate_button)
generate_button.clicked.connect(generate_story)

story_output = QTextEdit()
story_output.setReadOnly(True)
layout.addWidget(story_output)

window = QWidget()
window.setLayout(layout)
window.setWindowTitle('잼얘 생성기')
window.show()
app.exec()
