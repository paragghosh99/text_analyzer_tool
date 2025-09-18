import streamlit as st
from collections import Counter

st.title("📝 Text Analyzer Tool")

# Text input
user_text = st.text_area("Enter your text here:")
interactive_button = st.button("Analyze")

if user_text and interactive_button:
    # Basic stats
    char_count = len(user_text)
    word_count = len(user_text.split())
    sentence_count = user_text.count('.') + user_text.count('!') + user_text.count('?')

    st.write(f"**Characters:** {char_count}")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Sentences:** {sentence_count}")

    # Most common words
    words = user_text.lower().split()
    word_freq = Counter(words).most_common(3)

    st.subheader("Top 3 Words")
    for word, freq in word_freq:
        st.write(f"{word} → {freq}")
    