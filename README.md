

# 📘 AI Quiz Generator

An interactive **AI-powered Quiz Maker** that lets users paste any text (notes, articles, code explanations, etc.) and instantly create quizzes with **multiple-choice questions and correct answers**.

---

## 🚀 Key Features

* 📝 **Text Input** → Paste study notes, articles, or code.
* 🤖 **Automatic Quiz Creation** → AI generates 5–10 MCQs.
* 🎚 **Difficulty Settings** → Choose Easy / Medium / Hard.
* 🎯 **Answer Key** → Correct answers are clearly marked.
* 📊 **Prompting Styles**:

  * **Zero-Shot** → Direct quiz generation.
  * **One-Shot** → Guided with one sample Q\&A.
  * **Multi-Shot** → Guided with several examples.
  * **Chain-of-Thought** → AI explains its reasoning while creating questions.
* 📥 **Export Options** → Download quiz as `.txt` or `.pdf`.
* ⚡ Built using **Streamlit + Groq API (LLaMA 3.1)**.

---

## 🧠 GenAI Concepts Applied

1. **System & User Prompts** → Define AI as the quiz master.
2. **Zero-Shot Prompting** → Generate questions from text without examples.
3. **One-Shot Prompting** → Use one Q\&A example as guidance.
4. **Multi-Shot Prompting** → Provide multiple examples to shape responses.
5. **Chain-of-Thought Prompting** → Step-by-step reasoning (optional).
6. **Tokens & Tokenization** → Track usage and reduce costs.
7. **LLM Parameters** → Control creativity with Temperature, Top-p, and Max Tokens.
8. **Structured Output** → Results in `{question, options, answer}` format.

---

## 📂 Folder Layout

```
AI-Quiz-Generator/
│-- app.py               # Main Streamlit application
│-- src/
│   ├── groq_client.py   # Groq API calls + prompt handling
│-- requirements.txt     # Dependencies
│-- .env                 # GROQ_API_KEY stored here
│-- README.md            # Documentation
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2️⃣ Set Up Virtual Environment & Install Packages

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variable

Create a `.env` file in the root folder and add:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4️⃣ Start the App

```bash
streamlit run app.py
```

---

## 🖼️ Sample Run

**Input Text:**

> "Photosynthesis is the process where plants use sunlight to produce energy. Chlorophyll captures light, resulting in glucose and oxygen."

**Generated Quiz:**

1. Which pigment is key for photosynthesis?

   * a) Hemoglobin
   * b) Chlorophyll ✅
   * c) Melanin
   * d) Keratin

2. Which of these is a product of photosynthesis?

   * a) Carbon dioxide
   * b) Glucose ✅
   * c) Nitrogen
   * d) Salt

---

## 📌 Who Can Use This

* 🎓 **Students** → Turn notes into quick quizzes.
* 👨‍🏫 **Teachers** → Create practice tests instantly.
* 💻 **Developers** → Build quizzes from docs or code samples.

---

## 📜 License

MIT License © 2025

---
