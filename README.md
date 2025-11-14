# Streamlit GenAI Chat UI

## Overview
This is a simple Streamlit chat application that connects to an open
LLM hosted on Hugging Face (`meta-llama/Meta-Llama-3-8B-Instruct`).
The app includes a system prompt selector to change the model's behavior
(e.g., friendly assistant, strict expert, creative brainstormer).

## Features
- Chat-style interface using `st.chat_message` and `st.chat_input`.
- System prompt selector in the sidebar to control AI personality.
- Hugging Face Inference API integration using `InferenceClient`.
- Secrets stored securely in Streamlit Cloud (`HF_TOKEN`), not in code.

## Tech Stack
- Streamlit
- Hugging Face Hub (`huggingface_hub`)
- Open LLM: `meta-llama/Meta-Llama-3-8B-Instruct`
- Deployed on Streamlit Community Cloud
