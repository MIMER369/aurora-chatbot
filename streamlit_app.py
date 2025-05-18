import streamlit as st
import openai
from utils import load_api_key, load_products

# Load API key
openai.api_key = load_api_key()

# Page config
st.set_page_config(page_title="Aurora - Your E-Commerce AI Assistant", layout="centered")

# Matrix-themed CSS
st.markdown("""
<style>
body, .stApp {
    background-color: #0f0f0f;
    color: #00ff00;
    font-family: 'Courier New', Courier, monospace;
}
.stTextInput>div>div>input {
    background-color: #000000;
    color: #00ff00;
}
.stButton>button {
    background-color: #001100;
    color: #00ff00;
    border: 1px solid #00ff00;
}
.stChatMessage {
    background-color: #000000;
    color: #00ff00;
    border-left: 2px solid #00ff00;
    padding: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 AURORA")
st.subheader("Your E-Commerce AI Assistant")

# Load products
products = load_products()
if products:
    st.sidebar.header("Products Catalog")
    for p in products:
        st.sidebar.markdown(f"- **{p['name']}**: ${p['price']}")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)

# User input
if prompt := st.chat_input("Enter your query..."):
    st.session_state.history.append(("user", prompt))
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": r, "content": m} for r, m in st.session_state.history]
        )
        answer = response.choices[0].message.content
    except Exception:
        answer = "Sorry, something went wrong."
    st.session_state.history.append(("assistant", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
