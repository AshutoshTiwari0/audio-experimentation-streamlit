import streamlit as st
import speech_recognition as sr
import joblib
from joblib import load
st.title("Experimenting with Audio")

r = sr.Recognizer()

# Get audio from user
audio_value = st.audio_input("Record a voice message")

if audio_value is not None:
    # Save the recorded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_value.getvalue())

    # Use SpeechRecognition to read and recognize
    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data)
        st.success(f"You said: {text}")
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
else:
    st.info("Please record your voice to begin.")



if st.button('predict',key='output'):
    model = load("hate_speech.pkl")
    prediction = model.predict([text])  # 👈 wrap text in list
    if prediction[0] == 1:
        st.write("This is hate speech")
    else:
        st.write("This is not hate speech")