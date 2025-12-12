#VoiceBot UI with Gradio

import gradio as gr
import os
from doctor_brain import encode_image, analyze_image_with_query
from patient_voice import transcribe_with_groq
from doctor_voice import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

# --- SYSTEM PROMPT ---
system_prompt_base = """You have to act as a professional doctor.
Analyze the image and the patient's query.
If you make a differential, suggest some remedies. 
Do not add any numbers or special characters.
Your response should be in one long paragraph.
Do not say 'In the image I see', just start with your assessment.
Keep your answer concise (max 2 sentences)."""

def process_inputs(image_filepath, audio_filepath, text_input, language):
    # 1. Map code to full language name
    lang_map = {
        "en": "English", 
        "hi": "Hindi", 
        "es": "Spanish", 
        "fr": "French", 
        "de": "German"
    }
    target_language = lang_map.get(language, "English")

    # 2. Handle Audio vs Text Input
    speech_to_text_output = ""
    if audio_filepath:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
            audio_filepath=audio_filepath, 
            stt_model="whisper-large-v3",
            language=language
        )
    elif text_input:
        speech_to_text_output = text_input
    else:
        return "No input provided", "Please provide voice or text input.", None

    # 3. Analyze Image with Language Instruction
    if image_filepath:
        final_prompt = (
            f"{system_prompt_base}\n\n"
            f"Patient Query: {speech_to_text_output}\n"
            f"IMPORTANT: You must respond in the {target_language} language only."
        )
        
        doctor_response = analyze_image_with_query(
            query=final_prompt, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze."

    # 4. Generate Audio Response
    voice_of_doctor = text_to_speech_with_elevenlabs(doctor_response, "final.mp3")
    
    return speech_to_text_output, doctor_response, voice_of_doctor


# --- CUSTOM THEME SETTINGS ---
# Create a custom theme with specific colors
theme = gr.themes.Soft(
    primary_hue="teal",        # Main buttons and highlights will be Teal
    secondary_hue="emerald",   # Secondary elements will be Emerald Green
    neutral_hue="slate",       # Text and borders will be Slate Gray
).set(
    body_background_fill="#f0fdf4",  # Very light green background
    block_background_fill="#ffffff", # White boxes for inputs
    block_border_width="2px",
    block_title_text_weight="bold"
)

# Custom CSS for extra flair
custom_css = """
h1 {
    text-align: center;
    color: #0f766e;
    font-family: 'Arial', sans-serif;
}
.gradio-container {
    background: linear-gradient(to bottom right, #e0f2f1, #b2dfdb);
}
"""

# --- GRADIO INTERFACE ---
with gr.Blocks(theme=theme, css=custom_css, title="V.A.I.D. - Virtual AI Doctor") as demo:
    
    # Header Section
    gr.Markdown("# 🏥 V.A.I.D. (Virtual AI Doctor)")
    gr.Markdown("### *Intelligent Health Analysis with Vision & Voice*")
    
    with gr.Row():
        # --- LEFT COLUMN (Inputs) ---
        with gr.Column(scale=1):
            gr.Markdown("### 1. Upload Symptoms 📸")
            image_input = gr.Image(type="filepath", label="Upload Image", sources=["upload", "webcam"], height=300)
            
            gr.Markdown("### 2. Select Language 🌐")
            language_dropdown = gr.Dropdown(
                choices=[
                    ("English", "en"), 
                    ("Hindi", "hi"), 
                    ("Spanish", "es"), 
                    ("French", "fr"), 
                    ("German", "de")
                ], 
                value="en", 
                label="Language"
            )
            
            gr.Markdown("### 3. Describe Problem 🗣️")
            with gr.Tabs():
                with gr.TabItem("🎤 Voice Input"):
                    audio_input = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Record Voice")
                with gr.TabItem("⌨️ Text Input"):
                    text_input = gr.Textbox(label="Type Symptoms", placeholder="E.g., I have a red rash on my arm...", lines=2)
            
            # Big Submit Button
            submit_btn = gr.Button("👨‍⚕️ Consult V.A.I.D.", variant="primary", size="lg")

        # --- RIGHT COLUMN (Outputs) ---
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Patient Transcript")
            input_transcript = gr.Textbox(label="You Said:", lines=2, interactive=False)
            
            gr.Markdown("### 🩺 V.A.I.D. Diagnosis")
            doctor_text_output = gr.Textbox(
                label="Analysis", 
                lines=8, 
                interactive=False,
                show_label=False
            )
            
            gr.Markdown("### 🔊 Audio Response")
            audio_output = gr.Audio(label="Listen to Doctor", autoplay=True)

    # Footer
    gr.Markdown("---")
    gr.Markdown("*Disclaimer: V.A.I.D. is an AI project for educational purposes. Always consult a real doctor for medical advice.*")

    # Click Event
    submit_btn.click(
        fn=process_inputs,
        inputs=[image_input, audio_input, text_input, language_dropdown],
        outputs=[input_transcript, doctor_text_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch(debug=True)