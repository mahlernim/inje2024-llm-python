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
layout.addWidget(QLabel('Select a story style:'))
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

