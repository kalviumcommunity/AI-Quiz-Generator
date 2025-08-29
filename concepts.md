# 📘 **Concepts Covered**

### 1. **Create Project Readme**

* A clear `README.md` explains the **project idea**, **setup instructions**, **tech stack**, and **usage**.

---

### 2. **System & User Prompt**

* The **system prompt** sets the role: *“You are an AI tutor/quiz generator”*.
* The **user prompt** carries the actual **question/text/subject** entered by the user.

---

### 3. **Zero-Shot Prompting**

* AI answers the user’s question **without any examples**.
* Example: *“Explain Python lists.”* → Direct step-by-step explanation.

---

### 4. **One-Shot Prompting**

* AI is guided with **a single example Q\&A** before answering.
* Example: Shows *“Q: What is the boiling point of water? A: 100°C”* to help AI format.

---

### 5. **Multi-Shot Prompting**

* AI is given **multiple examples** to establish a pattern.
* Example: Water → 100°C, France → Paris, Shakespeare → Romeo & Juliet.
* Then AI applies the same structured style to new questions.

---

### 6. **Dynamic Prompting**

* Prompt **changes based on subject** (e.g., Science, History, Tech).
* Lets user **choose subject + number of quiz questions** dynamically.

---

### 7. **Chain-of-Thought Prompting (CoT)**

* AI is asked to **think step by step** before answering.
* Useful for reasoning-heavy questions (e.g., *“Why do we see phases of the moon?”*).

---

### 8. **Tokens & Tokenization**

* **Token usage logged** for each request.
* Tracks efficiency & cost monitoring when interacting with LLMs.
