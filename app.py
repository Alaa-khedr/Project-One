import streamlit as st
import whisper

st.title('Recordify ')

# Upload audio file with streamlit:
audio_file = st.file_uploader('Upload Audio', type=["wav", "mp3", "m4a", "mpeg", "ogg"])

try:
    model = whisper.load_model("base")
    st.text("Whisper Model Loaded")
except Exception as e:
    st.error(f"Error loading the Whisper model: {e}")
    st.stop()

if st.sidebar.button('Transcribe Audio'):
    if audio_file is not None:
        st.sidebar.success('Transcribing Audio')
        try:
            transcription = model.transcribe(audio_file.name)
            st.sidebar.success("Transcription Completed")
            st.markdown(transcription["text"])
        except Exception as e:
            st.error(f"Error transcribing audio: {e}")
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original File")
if audio_file is not None:
    st.sidebar.audio(audio_file)
else:
    st.sidebar.warning("No audio file uploaded")
