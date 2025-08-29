# 📘 AI Quiz Generator

An interactive **AI-powered Quiz Generator** where users can paste any text (article, notes, code explanation, etc.) and automatically generate quizzes with **questions, multiple-choice options, and correct answers**.

---

## 🚀 Features

* 📝 **Paste Text** → Input any notes, article, or code snippet.
* 🤖 **AI Quiz Generation** → AI generates 5–10 MCQs.
* 🎚 **Difficulty Levels** → Choose Easy / Medium / Hard.
* 🎯 **Answer Key** → Correct answers are highlighted.
* 📊 **Prompting Modes**:

  * **Zero-Shot** → Generate quiz directly.
  * **One-Shot** → Guided with one example Q\&A.
  * **Multi-Shot** → Guided with multiple examples.
  * **Chain-of-Thought** → AI explains reasoning behind quiz creation.
* 📥 **Export Option** → Save quiz as `.txt` or `.pdf`.
* ⚡ Built with **Streamlit + Groq API (LLaMA 3.1)**

---

## 🧠 GenAI Concepts Used

1. **System & User Prompts** → Define AI as quiz master.
2. **Zero-shot prompting** → Generate quiz from raw text.
3. **One-shot prompting** → Provide a sample Q\&A to guide.
4. **Multi-shot prompting** → Provide multiple examples.
5. **Chain-of-Thought prompting** → Step-by-step reasoning (optional).
6. **Tokens & Tokenization** → Track usage & optimize costs.
7. **LLM Parameters** → Temperature, Top-p, Max Tokens.
8. **Structured Output** → `{question, options, answer}` format.

---

## 📂 Project Structure

```
AI-Quiz-Generator/
│-- app.py                # Main Streamlit app
│-- src/
│   ├── groq_client.py    # Handles Groq API calls + prompting
│-- requirements.txt      # Dependencies
│-- .env                  # Store GROQ_API_KEY here
│-- README.md             # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repo

```bash
git clone https://github.com/yourusername/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2️⃣ Create Virtual Env & Install Requirements

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3️⃣ Add Environment Variable

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🖼️ Example Usage

**Input Text:**

> "Photosynthesis is the process by which plants convert sunlight into energy. Chlorophyll absorbs sunlight, producing glucose and oxygen."

**AI-Generated Quiz:**

1. What pigment is essential for photosynthesis?

   * a) Hemoglobin
   * b) Chlorophyll ✅
   * c) Melanin
   * d) Keratin

2. What is one main product of photosynthesis?

   * a) Carbon dioxide
   * b) Glucose ✅
   * c) Nitrogen
   * d) Salt

---

## 📌 Use Cases

* 🎓 Students → Quickly make quizzes from notes.
* 👨‍🏫 Teachers → Generate practice tests in seconds.
* 💻 Developers → Create technical quizzes from docs/code.

---

## 📜 License

MIT License © 2025