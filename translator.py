from transformers import pipeline
import streamlit as st

# Cache model loading to improve performance
@st.cache_resource
def load_model(model_name):
    return pipeline("translation", model=model_name)

# Available language pairs using Helsinki-NLP OPUS-MT models
def get_languages():
    return {
        "English to French": "Helsinki-NLP/opus-mt-en-fr",
        "French to English": "Helsinki-NLP/opus-mt-fr-en",
        "English to German": "Helsinki-NLP/opus-mt-en-de",
        "German to English": "Helsinki-NLP/opus-mt-de-en",
        "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
        "Spanish to English": "Helsinki-NLP/opus-mt-es-en",
        "English to Japanese": "Helsinki-NLP/opus-mt-en-jap",
        "Japanese to English": "Helsinki-NLP/opus-mt-jap-en",
        "English to Arabic": "Helsinki-NLP/opus-mt-en-ar",
        "Arabic to English": "Helsinki-NLP/opus-mt-ar-en",
        "English to Chinese": "Helsinki-NLP/opus-mt-en-zh",
        "Chinese to English": "Helsinki-NLP/opus-mt-zh-en",
        "English to Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "Hindi to English": "Helsinki-NLP/opus-mt-hi-en",
        "English to Italian": "Helsinki-NLP/opus-mt-en-it",
        "Italian to English": "Helsinki-NLP/opus-mt-it-en",
        "English to Russian": "Helsinki-NLP/opus-mt-en-ru",
        "Russian to English": "Helsinki-NLP/opus-mt-ru-en",
        "English to Dutch": "Helsinki-NLP/opus-mt-en-nl",
        "Dutch to English": "Helsinki-NLP/opus-mt-nl-en",
        "English to Portuguese": "Helsinki-NLP/opus-mt-en-pt",
        "Portuguese to English": "Helsinki-NLP/opus-mt-pt-en",
        "English to Korean": "Helsinki-NLP/opus-mt-en-ko",
        "Korean to English": "Helsinki-NLP/opus-mt-ko-en",
        "English to Turkish": "Helsinki-NLP/opus-mt-en-tr",
        "Turkish to English": "Helsinki-NLP/opus-mt-tr-en",
        "English to Greek": "Helsinki-NLP/opus-mt-en-el",
        "Greek to English": "Helsinki-NLP/opus-mt-el-en",
    }

# Function to translate text using the selected language model
def translate_text(text, lang_key):
    model = load_model(get_languages()[lang_key])
    translation = model(text)
    return translation[0]['translation_text']