import streamlit as st
from src.groq_client import (
    get_ai_response,
    build_zero_shot_prompt,
    build_one_shot_prompt,
    build_multi_shot_prompt,
    build_dynamic_prompt,
    build_cot_prompt
)

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Quiz & Tutor",  # Page title in browser
    page_icon="🧠",                # Page icon
    layout="wide"                  # Wide layout for better space usage
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("📘 Project Info")
    st.markdown("""**AI Personal Tutor + Quiz Generator**""")

    st.markdown("---")
    st.subheader("⚡ Try Example Inputs")
    st.markdown("""
    - What is React Hooks?  
    - Explain Python data types.  
    - How does blockchain work?  
    - Generate quiz from Climate Change.  
    """)

    st.markdown("---")
    st.subheader("🎯 Select Prompting Strategy")
    # Radio buttons to choose the prompting method
    prompt_type = st.radio(
        "Prompt Type:",
        ["Zero-Shot", "One-Shot", "Multi-Shot", "Dynamic", "Chain-of-Thought"]
    )

# -------------------------------
# Main Page
# -------------------------------
st.title("🧑‍🏫 AI Tutor & Quiz Generator")
st.write("Ask a question, or paste text to generate a quiz with different prompting strategies.")

# -------------------------------
# User Input
# -------------------------------
question = st.text_area("Enter your question or text:")  # Main input area
num_questions = st.number_input(
    "Number of Questions (for Quiz)", min_value=1, max_value=10, value=3
)  # Only used for quiz generation
subject = st.text_input(
    "Subject (only for Dynamic Prompting)",
    placeholder="e.g., Science, History"
)  # Dynamic prompting requires subject
submit = st.button("🚀 Generate Answer")  # Trigger AI response

# -------------------------------
# Processing
# -------------------------------
if submit and question:  # Only process if user clicked submit and entered text
    # -------------------------------
    # Build the prompt based on selected strategy
    # -------------------------------
    if prompt_type == "Zero-Shot":
        prompt = build_zero_shot_prompt("General", question)
    elif prompt_type == "One-Shot":
        prompt = build_one_shot_prompt("General", question)
    elif prompt_type == "Multi-Shot":
        prompt = build_multi_shot_prompt("General", question)
    elif prompt_type == "Dynamic":
        prompt = build_dynamic_prompt(question, subject, num_questions)
    elif prompt_type == "Chain-of-Thought":
        prompt = build_cot_prompt(question, num_questions)
    else:
        prompt = build_zero_shot_prompt("General", question)

    # -------------------------------
    # Call AI and show spinner while processing
    # -------------------------------
    with st.spinner("🤖 Thinking..."):
        answer = get_ai_response(prompt)

    # -------------------------------
    # Display result
    # -------------------------------
    st.success("✅ Response Generated!")
    st.markdown("### 📜 Answer / Quiz")
    st.write(answer)  # Display the AI’s answer or generated quiz
