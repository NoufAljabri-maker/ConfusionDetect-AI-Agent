# 🧠 ConfusionDetect AI Agent

**ConfusionDetect** is an adaptive AI teaching agent that detects student misconceptions, evaluates understanding, and changes its teaching strategy based on the student's responses.

Unlike a traditional chatbot that simply provides an answer, ConfusionDetect follows an iterative **diagnose → evaluate → decide → adapt** process to help students correct misunderstandings.

---

## 🎯 Project Goal

Students often have misconceptions rather than simply missing information.

For example:

> "I think RAM and hard disk are the same because both store data."

Instead of immediately giving the correct answer, ConfusionDetect:

1. Analyzes the student's statement.
2. Detects the misconception.
3. Identifies the subject and topic.
4. Generates a diagnostic question.
5. Evaluates the student's answer.
6. Determines the student's understanding level.
7. Selects the next teaching action.
8. Re-evaluates the student when necessary.

---

## 🤖 Agent Workflow

```text
Student Input
      ↓
Detect Misconception
      ↓
Ask Diagnostic Question
      ↓
Student Answer
      ↓
Evaluate Understanding
      ↓
┌─────────────────────────┐
│ UNDERSTOOD              │
│ PARTIALLY_UNDERSTOOD    │
│ STILL_CONFUSED          │
└────────────┬────────────┘
             ↓
Choose Teaching Strategy
             ↓
Re-explain / Ask Again
             ↓
Re-evaluate
             ↺
```

The loop continues until the student demonstrates understanding or reaches the maximum number of attempts.

---

## ✨ Key Features

- 🧠 Misconception detection
- 📚 Subject and topic identification
- ❓ Diagnostic question generation
- 🔍 Student-answer evaluation
- 🎯 Understanding-level classification
- 🔄 Adaptive teaching strategy
- 🧩 Multi-step Agent Loop
- 📝 Session state and interaction history
- 💻 Local LLM execution
- 🔐 No paid API required
- 🌐 Streamlit user interface

---

## 🧠 Agent Decision Making

The agent classifies student understanding into three states:

### ✅ UNDERSTOOD

The student demonstrates correct understanding and the learning session can be completed.

### 🟡 PARTIALLY_UNDERSTOOD

The student understands part of the concept but still has gaps. The agent changes its teaching approach and asks another question.

### 🔴 STILL_CONFUSED

The misconception is still present. The agent simplifies the explanation and generates a new diagnostic question.

---

## 🤖 Why Is This an AI Agent?

ConfusionDetect is designed as more than a question-answer chatbot.

It demonstrates key agentic characteristics:

- **Goal:** Resolve the student's misconception.
- **Observation:** Analyze student statements and responses.
- **Reasoning:** Diagnose misconceptions and evaluate understanding.
- **Decision Making:** Determine the student's current understanding level.
- **Action:** Select an appropriate teaching response.
- **Adaptation:** Change the teaching strategy when needed.
- **State:** Track attempts and interaction history.
- **Loop:** Continue evaluating until the learning goal is achieved.

### Agent Cycle

**Observe → Diagnose → Ask → Evaluate → Decide → Adapt → Re-evaluate**

---

## 🛠️ Technologies

- Python
- Streamlit
- Ollama
- Llama 3.2
- Local Large Language Model (LLM)

---

## 📁 Project Structure

```text
ConfusionDetect-AI-Agent/
│
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

**app.py**  
Streamlit interface, session state, attempt tracking, and Agent Loop.

**agent.py**  
Misconception analysis, diagnostic questioning, answer evaluation, and adaptive teaching decisions.

**tools.py**  
Reserved for future agent tools and extensions.

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/NoufAljabri-maker/ConfusionDetect-AI-Agent.git
```

### 2. Enter the project directory

```bash
cd ConfusionDetect-AI-Agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\\Scripts\\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and prepare Ollama

```bash
ollama pull llama3.2
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

---

## 🧪 Example

### Student Input

> I think RAM and hard disk are the same because both store data.

### Agent Diagnosis

The agent detects that the student is confusing **temporary volatile memory** with **persistent storage**.

### Diagnostic Question

> What happens to the data stored in RAM when the computer is turned off?

If the student answers incorrectly:

**STILL_CONFUSED → Re-explain → Ask another question**

If the student demonstrates correct understanding:

**UNDERSTOOD → Complete the learning session**

---

## 🚀 Future Work

- Long-term student memory
- Personalized learning profiles
- Retrieval-Augmented Generation (RAG)
- Subject-specific agent tools
- Teacher analytics dashboard
- Student progress tracking
- Multi-agent collaboration

---

## ⚠️ Disclaimer

ConfusionDetect is an educational prototype developed to demonstrate adaptive AI Agent behavior.

It is not intended to replace teachers or formal educational assessment.

---

## 👩‍💻 Author

**Nouf Aljabri**  
Computer Science
