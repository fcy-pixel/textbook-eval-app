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
iframe { border: none !important; height: 100vh !important; }
[data-testid="stAppViewContainer"] { padding: 0; }
section[data-testid="stMain"] > div { padding: 0; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=10000, scrolling=True)
