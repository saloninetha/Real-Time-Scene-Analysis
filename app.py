import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file
from google.generativeai import configure
from dotenv import load_dotenv
from PIL import Image
import tempfile
from pathlib import Path
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    configure(api_key=API_KEY)

# Streamlit page config
st.set_page_config(
    page_title="Multimodal AI Agent - Webcam Image Analyzer",
    page_icon="📸",
    layout="wide"
)

st.title("Real Time Scene Detection 🎥🎤🖬")
st.header("Powered by Gemini 2.0 Flash Exp")

# Initialize Phi Agent with Gemini
@st.cache_resource
def initialize_agent():
    return Agent(
        name="Webcam Image Analyzer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

multimodal_Agent = initialize_agent()

# Webcam input (image only)
camera_image = st.camera_input("Click a picture using your webcam")

if camera_image:
    image = Image.open(camera_image)
    st.image(image, caption="Captured Image", use_container_width=True)  


    user_query = st.text_area(
        "What insights are you seeking from the webcam picture?",
        placeholder="Ask anything about the photo content. The AI agent will analyze and gather additional context if needed.",
        help="Provide specific questions or insights you want from the webcam photo."
    )

    if st.button("🔍 Analyze Webcam Photo", key="analyze_webcam_photo_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the photo.")
        else:
            try:
                with st.spinner("Uploading image and analyzing..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_img:
                        temp_img_path = temp_img.name
                        image.save(temp_img_path)

                    uploaded = upload_file(temp_img_path)

                    # Optional: Delete temp file
                    try:
                        Path(temp_img_path).unlink(missing_ok=True)
                    except Exception as e:
                        st.warning(f"Could not delete temp file {temp_img_path}: {e}")

                    # Prompt Gemini
                    analysis_prompt = f"""
                    Analyze the visual content of the uploaded photo.

                    User query: {user_query}

                    Please provide a clear, concise, and contextually rich response using insights from the image and external knowledge.
                    """

                    response = multimodal_Agent.run(analysis_prompt, images=[uploaded])

                    # Display result
                    st.subheader("Analysis Result")
                    st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
else:
    st.info("Use the webcam to capture a photo for analysis.")

# Custom CSS styling
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)