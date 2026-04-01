import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="課本評選系統",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI for a cleaner look
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=2000, scrolling=True)
