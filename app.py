import streamlit as st
import os
import glob
from gtts import gTTS


try:
    os.mkdir("temp")
except:
    pass

speech_file = "speech.mp3"

mp3_file = glob.glob("temp/*mp3")
for f in mp3_file:
  os.remove(f)
  print("Deleted",f)

st.title("Text to speech")

# text = st.text_input("文章を入力して下さい")
text = st.text_area("文章を入力して下さい",placeholder="Write Here")

def text_to_speech(text):
  tts = gTTS(text, lang="ja")
  tts.save(f"temp/{speech_file}")

if text != "":
  with st.spinner("In progress..."):
    text_to_speech(text)
    audio_file = open(f"temp/{speech_file}", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## 朗読")
    st.audio(audio_bytes, format="audio/mp3", start_time = 0)



