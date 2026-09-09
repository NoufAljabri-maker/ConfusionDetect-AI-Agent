# 🧠 ConfusionDetect AI Agent

**ConfusionDetect** is an adaptive AI teaching agent designed to detect student misconceptions, evaluate understanding, and autonomously adapt its teaching strategy.

Unlike a traditional chatbot that simply answers questions, ConfusionDetect follows an iterative decision-making process to help students correct misunderstandings.

---

## 🎯 Project Goal

Students often have misconceptions rather than simply missing information.

For example:

> "I think RAM and hard disk are the same because both store data."

Instead of immediately providing the correct answer, ConfusionDetect diagnoses the misconception, asks a targeted question, evaluates the student's response, and decides what teaching action should happen next.

---

## 🤖 How the AI Agent Works

The agent follows this adaptive learning cycle:

```text
Student Input
      ↓
Detect Misconception
      ↓
Identify Subject & Topic
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
Re-explain / Follow-up Question
             ↓
Re-evaluate
             ↺
```

The cycle continues until the student demonstrates understanding or the maximum number of attempts is reached.

---

## ✨ Main Features

- 🧠 Misconception detection
- 📚 Subject and topic identification
- ❓ Automatic diagnostic question generation
- 🔍 Student answer evaluation
- 🎯 Understanding-level classification
- 🔄 Adaptive teaching strategy
- 🧩 Multi-step Agent Loop
- 📝 Interaction history
- 💻 Local LLM execution
- 🔐 No paid API required
- 🌐 Interactive Streamlit interface

---

## 🧠 Understanding Levels

The agent classifies the student's response into three levels:

### ✅ UNDERSTOOD
The student demonstrates correct understanding. The agent confirms the understanding and can provide a mini-quiz question.

### 🟡 PARTIALLY_UNDERSTOOD
The student understands part of the concept but still has gaps. The agent changes its teaching strategy, provides a simpler explanation or analogy, and asks another question.

### 🔴 STILL_CONFUSED
The original misconception is still present. The agent simplifies the explanation and generates another diagnostic question.

---

## 🔄 Agent Decision Loop

ConfusionDetect follows an iterative agent cycle:

**Observe → Diagnose → Ask → Evaluate → Decide → Adapt → Re-evaluate**

The agent maintains the current learning session, tracks attempts, evaluates student responses, and decides what action should happen next.

A maximum of three attempts is currently used to prevent an unlimited interaction loop.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Local Large Language Model (LLM)

---

## 📁 Project Structure

    ConfusionDetect-AI-Agent/
    │
    ├── app.py
    ├── agent.py
    ├── tools.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

### `app.py`

Provides the Streamlit interface and manages session state, student interaction, attempt tracking, agent status, decision history, and the Agent Loop.

### `agent.py`

Contains the main AI Agent logic, including misconception analysis, diagnostic questioning, answer evaluation, understanding classification, and teaching-strategy selection.

### `tools.py`

Reserved for additional agent tools and future extensions.

---

## 💻 Installation

### 1. Clone the repository

    git clone https://github.com/NoufAljabri-maker/ConfusionDetect-AI-Agent.git

Then enter the project directory:

    cd ConfusionDetect-AI-Agent

### 2. Create a virtual environment

    python -m venv venv

On Windows, activate it using:

    venv\Scripts\activate.bat

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Install Ollama

Install Ollama and download the Llama 3.2 model:

    ollama pull llama3.2

Test the model:

    ollama run llama3.2

### 5. Run the application

    python -m streamlit run app.py

The Streamlit application will then open locally in your browser.

---

## 🧪 Example

### Student Input

> I think RAM and hard disk are the same because both store data.

### Agent Behavior

The agent detects that the student is confusing temporary volatile memory with persistent storage.

It then asks a diagnostic question such as:

> What happens to the data stored in RAM when the computer is turned off?

If the student's answer is incorrect, the agent may classify the understanding as:

**STILL_CONFUSED**

The agent then changes its teaching strategy and continues the learning loop.

When the student demonstrates correct understanding, the agent classifies the response as:

**UNDERSTOOD**

---

## 🤖 Why Is This an AI Agent?

ConfusionDetect is designed as more than a traditional question-answer chatbot.

It demonstrates several important AI Agent characteristics:

1. **Goal-oriented behavior** — Its goal is to reduce the student's misconception.

2. **Observation** — It observes the student's initial statement and subsequent answers.

3. **Reasoning and diagnosis** — It identifies misconceptions and evaluates understanding.

4. **Decision making** — It determines whether the student has understood, partially understood, or remains confused.

5. **Adaptive action** — It changes the teaching strategy according to the student's understanding.

6. **State tracking** — It maintains attempts and interaction history.

7. **Iterative behavior** — It repeatedly evaluates and adapts until the learning goal is achieved or the attempt limit is reached.

---

## 🚀 Future Improvements

Future versions could include:

- Long-term student memory
- Personalized learning profiles
- Retrieval-Augmented Generation (RAG)
- Subject-specific tools
- Teacher analytics dashboard
- Student progress tracking
- Multiple teaching strategies
- Multi-agent collaboration

---

## ⚠️ Disclaimer

ConfusionDetect is an educational prototype developed to demonstrate adaptive AI Agent concepts.

It is not intended to replace teachers or formal educational assessment.

---

## 👩‍💻 Author

**Nouf Aljabri**

Computer Science 
