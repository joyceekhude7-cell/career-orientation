import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="Career Orientation Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🎓 Career Orientation Chatbot")
st.write("Ask questions about careers, skills, resumes, interviews, and more!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        response = get_answer(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )