# 🏥 V.A.I.D. (Virtual AI Doctor)

> **Intelligent Health Analysis with Vision & Voice**
> *A Multilingual AI Doctor powered by Llama 4, Whisper, and ElevenLabs.*



## 📖 Overview

**V.A.I.D.** (Virtual AI Doctor) is an advanced telemedicine prototype designed to bridge the gap between patients and medical advice using multimodal AI. It simulates a real doctor-patient interaction by "seeing" symptoms, "hearing" concerns in multiple languages, and "speaking" back with professional advice.

### Key Capabilities:
1.  **👁️ Vision:** Diagnoses medical issues from uploaded images using the **Llama 4 Multimodal** model.
2.  **🗣️ Voice:** Listens to patients in **Hindi, English, Spanish, etc.** using **Whisper v3**.
3.  **🔊 Speech:** Responds with a human-like voice using **ElevenLabs Multilingual v2**.
4.  **💬 Text Support:** Includes a fallback text chat for users who prefer typing.

---

## ✨ Features

* **Multimodal Analysis:** Combines image + audio data for accurate diagnosis.
* **Multilingual Support:** Speaks and understands **English, Hindi, Spanish, French, and German**.
* **Smart Medical UI:** A professional interface built with **Gradio Blocks**, featuring custom themes and organized tabs.
* **Real-time Processing:** Fast inference using Groq's LPU (Language Processing Unit).

---

## 🛠️ Tech Stack

| Component | Technology Used |
| :--- | :--- |
| **Brain (LLM)** | **Llama-4-Scout-17b** (via Groq Cloud) |
| **Ears (STT)** | **Whisper-Large-v3** (via Groq Cloud) |
| **Voice (TTS)** | **ElevenLabs Multilingual v2** |
| **Frontend** | **Gradio (Python)** |
| **Audio Tools** | FFmpeg, PyDub, SpeechRecognition |

---

## ARCHITECTURE
<img width="1000" height="569" alt="image" src="https://github.com/user-attachments/assets/20c54acb-c0a8-4d4b-ad07-3d4130fe167e" />

## DEMO (ENGLISH VERSION)
<img width="1896" height="880" alt="image" src="https://github.com/user-attachments/assets/622a8fbd-7792-4902-9912-175e0db636cc" />

## DEMO (HINDI VERSION)
<img width="1481" height="771" alt="image" src="https://github.com/user-attachments/assets/72ba1721-3bfe-4978-a15f-d435d810d9be" />



