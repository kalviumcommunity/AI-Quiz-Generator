import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("⚠️ GROQ_API_KEY not found in .env file!")

# Model
MODEL_NAME = "llama-3.1-8b-instant"
