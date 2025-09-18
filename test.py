import streamlit as st
from collections import Counter

st.title("Text Analyzer Tool")

# user_words = st.text_area("Enter your text here")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Inc"):
    st.session_state.count += 1

st.write("Count:", st.session_state.count)
