from groq import Groq
from src.config import GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# ==============================
# Prompt Builders
# ==============================


def build_zero_shot_prompt(text, num_questions):
    """
    Zero-Shot: AI generates quiz questions without examples.
    """
    return f"""
You are an AI tutor. 
Generate {num_questions} multiple-choice quiz questions from the text below.
Each question should have 4 options (A–D) and specify the correct answer.

Text:
{text}
"""


def build_one_shot_prompt(text, num_questions):
    """
    One-Shot: AI is given a single example.
    """
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
    """
    Multi-Shot: AI is given multiple examples.
    """
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
    """
    Dynamic Prompting: AI adapts based on subject chosen by user.
    """
    return f"""
You are an AI tutor specializing in {subject}.
Generate {num_questions} quiz questions for {subject} based on the text below.
Each question should include 4 options and specify the correct answer.

Text:
{text}
"""


def build_cot_prompt(text, num_questions):
    """
    Chain-of-Thought: AI must explain reasoning step by step.
    """
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
    Calls the Groq LLM with the provided prompt.
    Supports streaming with the smaller 8B instant model.
    Logs tokens if stream=False.
    """
    if stream:
        # Streaming response
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
            print(content, end="", flush=True)
            response_text += content
        print()  # newline after streaming
        return response_text

    else:
        # Standard response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=800,
        )

        if hasattr(response, "usage"):
            tokens_used = response.usage.total_tokens
            print(f"✅ Tokens used: {tokens_used}")

        return response.choices[0].message.content
