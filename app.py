import streamlit as st
from huggingface_hub import InferenceClient

# ---------------- Page Setup ----------------
st.set_page_config(page_title="GenAI Chat", page_icon="🤖")

st.title("🤖 GenAI Chat with System Prompt Selector")

# Different "personalities" for the AI
SYSTEM_PROMPTS = {
    "Friendly Assistant": "You are a warm, friendly assistant. Explain things simply.",
    "Strict Expert": "You are a precise, no-nonsense expert. Be concise and technical.",
    "Creative Brainstormer": "You are a creative collaborator. Suggest ideas and think out loud."
}

# Read Hugging Face token from Streamlit secrets (set in Streamlit Cloud)
HF_TOKEN = st.secrets["HF_TOKEN"]

# Create a client to talk to the LLM
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN,
)

# ---------------- Sidebar: System Prompt Selector ----------------
system_choice = st.sidebar.selectbox(
    "Choose system behavior:",
    list(SYSTEM_PROMPTS.keys())
)
system_prompt = SYSTEM_PROMPTS[system_choice]

st.sidebar.write("**Active system prompt:**")
st.sidebar.caption(system_prompt)

# ---------------- Chat History ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- User Input ----------------
user_input = st.chat_input("Ask me something...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message in the UI
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build messages list for LLM: system + history
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(st.session_state.messages)

    # Ask the model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat_completion(
                messages=messages,
                max_tokens=256,
            )
            assistant_reply = response.choices[0].message["content"]
            st.markdown(assistant_reply)

    # Save assistant reply to history
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )
