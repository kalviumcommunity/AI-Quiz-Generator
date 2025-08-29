from groq import Groq
from src.config import GROQ_API_KEY

# Initialize Groq client using API key from config file
client = Groq(api_key=GROQ_API_KEY)

# ==============================
# Prompt Builders
# ==============================

def build_zero_shot_prompt(text, num_questions):
    """Zero-Shot: AI generates quiz questions without any examples."""
    return f"""
You are an AI tutor. 
Generate {num_questions} multiple-choice quiz questions from the text below.
Each question should have 4 options (A–D) and specify the correct answer.

Text:
{text}
"""

def build_one_shot_prompt(text, num_questions):
    """One-Shot: AI is given a single example to guide its response."""
    example = """
Q: What is the capital of France?
A) Berlin
B) Paris
C) Madrid
D) Rome
Correct Answer: B) Paris
"""
    return f"""
You are an AI tutor. 
Here is an example format:
{example}

Now, generate {num_questions} new multiple-choice quiz questions from the text below.
Each should include 4 options and the correct answer.

Text:
{text}
"""

def build_multi_shot_prompt(text, num_questions):
    """Multi-Shot: AI is given multiple examples to improve consistency."""
    examples = """
Example 1:
Q: What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
Correct Answer: B) 4

Example 2:
Q: Who wrote 'Romeo and Juliet'?
A) Charles Dickens
B) William Shakespeare
C) Mark Twain
D) Jane Austen
Correct Answer: B) William Shakespeare
"""
    return f"""
You are an AI tutor. 
Here are some examples:
{examples}

Now, generate {num_questions} multiple-choice quiz questions from the text below.
Each should include 4 options and the correct answer.

Text:
{text}
"""

def build_dynamic_prompt(text, subject, num_questions):
    """Dynamic Prompting: AI adapts based on subject chosen by user."""
    return f"""
You are an AI tutor specializing in {subject}.
Generate {num_questions} quiz questions for {subject} based on the text below.
Each question should include 4 options and specify the correct answer.

Text:
{text}
"""

def build_cot_prompt(text, num_questions):
    """Chain-of-Thought (CoT): AI must explain its reasoning step by step."""
    return f"""
You are an AI tutor who explains reasoning step by step.
Generate {num_questions} multiple-choice quiz questions from the text below.
For each answer, explain your reasoning briefly.

Text:
{text}
"""

# ==============================
# API Caller
# ==============================

def get_ai_response(prompt, stream=False):
    """
    Sends the prompt to the Groq LLM and gets the AI's response.
    - Supports streaming responses (token by token).
    - Uses 'llama-3.1-8b-instant' model.
    - Logs token usage for cost/performance monitoring.
    """
    if stream:
        # Streaming response: AI outputs text in chunks
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=800,
            top_p=1,
            stream=True,
        )

        response_text = ""
        for chunk in completion:
            delta = chunk.choices[0].delta
            content = delta.get("content", "")
            print(content, end="", flush=True)  # live output
            response_text += content
        print()  
        return response_text

    else:
        # Standard (non-streaming) response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=800,
        )

        # ✅ Log token usage clearly
        if hasattr(response, "usage"):
            print("📊 Token Usage Stats:")
            print(f"   📝 Prompt tokens     : {response.usage.prompt_tokens}")
            print(f"   💡 Completion tokens : {response.usage.completion_tokens}")
            print(f"   🔢 Total tokens      : {response.usage.total_tokens}")
            print("-" * 40)

        # Return the AI's final text
        return response.choices[0].message.content
