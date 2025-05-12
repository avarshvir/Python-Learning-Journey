import streamlit as st
import speech_recognition as sr

# Function to capture voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "Error with the recognition service"

# Sidebar with conversation topics
st.sidebar.title("Copilot")
st.sidebar.subheader("Conversations")
st.sidebar.text("Today")
st.sidebar.text("Introduction to Copilot Au...")
st.sidebar.text("Yesterday")
st.sidebar.text("Rejecting Stereotypes and...")
st.sidebar.text("Previous week")
st.sidebar.text("SQLite3 in Requirements.fx...")
st.sidebar.text("Imagining a Flying Dragon")

# Main section with greeting message
st.markdown("<h1 style='text-align: center;'>Good evening, arshvir</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>What can I help you with today?</h2>", unsafe_allow_html=True)

# Text input field
user_input = st.text_input("Message Copilot")

# Button for microphone input
if st.button("🎤 Speak"):
    spoken_text = recognize_speech()
    st.text(f"Recognized: {spoken_text}")