import streamlit as st
import re
from collections import Counter
import pandas as pd

st.title("Text Analyzer Tool")

if "count" not in st.session_state:
    st.session_state.count = 0

user_words = st.text_area("Enter your text here")

if st.button("Analyze"):
    if not user_words.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        char_count = len(user_words)
        word_count = len(user_words.split())
        sentence_count = user_words.count('.') + user_words.count('!') + user_words.count('?')

        words = re.findall(r"\b\w+\b", user_words.lower())
        word_freq = Counter(words).most_common(5)

        st.write(f"Character count: {char_count}")
        st.write(f"Word count: {word_count}")
        st.write(f"Sentence count: {sentence_count}")
        st.write("### Top 5 words ->")
        c1, c2 = st.columns(2)
        for word, freq in word_freq:
            with c1: st.write(word)
            with c2: st.write(freq)
        
        df = pd.DataFrame(word_freq, columns=["Word", "Frequency"])

        st.bar_chart(df.set_index("Word"))

        if st.button("Reset"):
            st.session_state.count = 0
        else:
            st.session_state.count += 1

st.write("Number of analyses performed: ", st.session_state.count)