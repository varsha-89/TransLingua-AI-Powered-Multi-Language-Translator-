import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="TransLingua – AI Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.header-box {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    border-radius: 25px;
    padding: 28px;
    margin-bottom: 35px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.header-title {
    font-size: 42px;
    font-weight: 800;
}
.header-subtitle {
    font-size: 16px;
    color: #cfd8dc;
}
.glass {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border-radius: 22px;
    padding: 30px;
}
.result-box {
    background: rgba(0, 255, 150, 0.15);
    border-left: 6px solid #00e676;
    padding: 18px;
    border-radius: 10px;
    font-size: 20px;
    margin-top: 15px;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <div class="header-title">🌍 TransLingua</div>
    <div class="header-subtitle">
        AI-Powered Multi-Language Translator (Text + Voice)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)

translator = Translator()

# ---------------- INPUT ----------------
text = st.text_area("✍️ Enter text to translate", height=120)

# ---------------- LANGUAGE MAP ----------------
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Korean": "ko",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

languages = list(lang_map.keys())

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("🌐 Source Language", languages, index=0)
with col2:
    target_lang = st.selectbox("🎯 Target Language", languages, index=languages.index("Telugu"))

# ---------------- TRANSLATION ----------------
if st.button("🚀 Translate", use_container_width=True):
    if text.strip() == "":
        st.warning("⚠️ Please enter text")
    else:
        translated = translator.translate(
            text,
            src=lang_map[source_lang],
            dest=lang_map[target_lang]
        )

        st.markdown("### ✅ Translation Result")
        st.markdown(
            f"<div class='result-box'>{translated.text}</div>",
            unsafe_allow_html=True
        )

        # 🔊 TEXT TO SPEECH
        tts = gTTS(text=translated.text, lang=lang_map[target_lang])

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            audio_path = fp.name

        st.markdown("### 🔊 Listen Translation")
        st.audio(audio_path)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;color:#9e9e9e;margin-top:20px;'></p>",
    unsafe_allow_html=True
)
