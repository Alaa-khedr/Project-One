import streamlit as st
import whisper
import os

# Specify the path to the FFmpeg executable
ffmpeg_path = "/path/to/ffmpeg"  # Update with the correct path

# Set the FFmpeg executable path
os.environ["FFMPEG_BINARY"] = ffmpeg_path

# Rest of your Streamlit code


st.title('Recordify ')

# upload audio file with streamlit:
audio_file = st.file_uploader('Upload Audio', type=["wav", "mp3", "m4a", "mpeg", "ogg"])

model = whisper.load_model("base")
st.text("Whisper Model Loaded")
    
if st.sidebar.button('Transcribe Audio'):
    if audio_file is not None:
        st.sidebar.success('Transcribing Audio')
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Completed")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original File")
st.sidebar.audio(audio_file)