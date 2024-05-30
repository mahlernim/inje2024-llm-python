import streamlit as st
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key='yourapikey')

hidden_history = [
    {"role": "model", "parts": ["야 뭐하냐?"]}
]

model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction="당신은 까칠한 친구입니다. 늘 빈정거리지만 사실 유저를 매우 챙기고 있습니다. 친구와 채팅하듯 편하고 짤막하게 답하시오.")
chat = model.start_chat(history=hidden_history)

# Streamlit application
st.title("츤데레봇")

if 'conversation' not in st.session_state:
    st.session_state.conversation = [("친구", "야 뭐하냐?")]

def send_message():
    user_input = st.session_state.user_input
    st.session_state.conversation.append(("나", user_input))
    
    if user_input in ['끝', '종료', '대화종료']:
        st.session_state.conversation.append(("친구", "ㅂㅂ\n(친구가 접속을 종료했습니다.)"))
    else:
        response = chat.send_message(user_input)
        model_message = response.text.replace('\n\n', '\n').strip()
        st.session_state.conversation.append(("친구", model_message))
    
    st.session_state.user_input = ""  # Clear the input after sending the message

# Display the conversation
for sender, message in st.session_state.conversation:
    st.write(f"**{sender}:** {message}")

# Add a placeholder at the bottom for the text input
st.text_input("나:", key="user_input", on_change=send_message)

# To run the app, use the command: streamlit run <script_name>.py
