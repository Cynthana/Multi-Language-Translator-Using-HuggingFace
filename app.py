import streamlit as st
from translator import translate_text, get_languages

# Streamlit app UI
st.title("🌍 Multi-Language Translator")

st.markdown("Translate text between multiple languages using AI-powered translation models.")

# Dropdown to select language pair
languages = get_languages()
selected_lang = st.selectbox("Choose translation:", list(languages.keys()))

# Input text box
text_input = st.text_area("Enter text to translate:")

# Translation button
if st.button("Translate"):
    if text_input.strip():
        translated_text = translate_text(text_input, selected_lang)
        st.success(f"✅ Translation: **{translated_text}**")
    else:
        st.warning("⚠️ Please enter text to translate.")