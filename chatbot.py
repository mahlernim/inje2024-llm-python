import streamlit as st
import google.generativeai as genai

# API 키 설정
genai.configure(api_key='yourapikey')

# 모델 초기화
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="당신은 유저의 친한 친구입니다. 비아냥대며 차갑게 굴지만 사실 굉장히 친구를 아끼고 좋아합니다. 채팅하듯 짤막한 답변을 하세요.")
chat = model.start_chat(history=[])

# Streamlit UI 구성
st.title("츤데레 챗봇")

if 'history' not in st.session_state:
    st.session_state.history = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

def send_message():
    user_input = st.session_state.user_input
    if user_input:
        for i in range(5):
            try:
                response = chat.send_message(user_input)
            except:
                print(i)
                continue
            else:
                break
        reply = response.text.replace("\n\n", "\n").strip()
        st.session_state.history.append(f"나: {user_input}")
        st.session_state.history.append(f"친구: {reply}")
        st.session_state.user_input = ""  # 입력 필드 초기화

# 대화 기록 출력
for line in st.session_state.history:
    st.write(line)

# user input
st.text_input("나: ", key='user_input', on_change=send_message)

