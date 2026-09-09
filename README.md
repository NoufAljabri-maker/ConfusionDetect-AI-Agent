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

The agent classifies the student's understanding into three levels:

### ✅ UNDERSTOOD

The student demonstrates correct understanding. The agent confirms the student's understanding and completes the learning session.

### 🟡 PARTIALLY_UNDERSTOOD

The student understands part of the concept but still has gaps.

The agent changes its teaching strategy, provides a simpler explanation or analogy, and asks another question.

### 🔴 STILL_CONFUSED

The original misconception is still present.

The agent simplifies the explanation and generates another diagnostic question.

---

## 🔄 Agent Decision Loop

ConfusionDetect follows an iterative agent cycle:

**Observe → Diagnose → Ask → Evaluate → Decide → Adapt → Re-evaluate**

The agent maintains the current learning session, tracks attempts, evaluates student responses, and determines what action should happen next.

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

### `app.py`

Provides the Streamlit user interface and manages:

- Session state
- Student interaction
- Attempt tracking
- Agent status
- Decision history
- Agent Loop

### `agent.py`

Contains the main AI Agent logic, including:

- Misconception analysis
- Diagnostic question generation
- Student answer evaluation
- Understanding classification
- Adaptive teaching decisions

### `tools.py`

Reserved for additional agent tools and future extensions.

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/NoufAljabri-maker/ConfusionDetect-AI-Agent.git
```

Enter the project directory:

```bash
cd ConfusionDetect-AI-Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows, activate the environment:

```bash
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama on your computer.

Then download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Test the model:

```bash
ollama run llama3.2
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The Streamlit application will then open locally in your browser.

---

## 🧪 Example

### Student Input

> I think RAM and hard disk are the same because both store data.

### Agent Diagnosis

The agent detects that the student is confusing temporary volatile memory with persistent storage.

### Diagnostic Question

> What happens to the data stored in RAM when the computer is turned off?

If the student's answer is incorrect, the agent may classify the student's understanding as:

**STILL_CONFUSED**

The agent then changes its teaching strategy, provides another explanation, and continues the learning loop.

When the student demonstrates correct understanding, the agent may classify the response as:

**UNDERSTOOD**

The learning session can then be completed.

---

## 🤖 Why Is This an AI Agent?

ConfusionDetect is designed as more than a traditional question-answer chatbot.

It demonstrates several key AI Agent characteristics:

### 1. Goal-Oriented Behavior

The agent has a clear goal: **reduce or resolve the student's misconception**.

### 2. Observation

The agent observes the student's initial statement and subsequent responses.

### 3. Reasoning and Diagnosis

It analyzes the student's input to identify the academic topic and possible misconception.

### 4. Decision Making

The agent evaluates the student's answer and decides whether the student is:

- UNDERSTOOD
- PARTIALLY_UNDERSTOOD
- STILL_CONFUSED

### 5. Adaptive Action

Based on its evaluation, the agent changes its teaching strategy and determines the next action.

### 6. State Tracking

The system maintains the current session, number of attempts, and interaction history.

### 7. Iterative Behavior

The agent repeatedly evaluates and adapts until the learning goal is achieved or the maximum number of attempts is reached.

---

## 🏗️ Agent Architecture

```text
                    ┌───────────────────┐
                    │   Student Input   │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Misconception     │
                    │ Diagnosis         │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Diagnostic        │
                    │ Question          │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Student Response  │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Understanding     │
                    │ Evaluation        │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Decision Engine   │
                    └─────────┬─────────┘
                              ↓
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
         UNDERSTOOD       PARTIALLY       STILL
                          UNDERSTOOD       CONFUSED
              ↓               ↓               ↓
          Complete         Adapt           Re-teach
                           Strategy
                              ↓
                         Re-evaluate
                              ↺
```

---

## 🚀 Future Improvements

Future versions could include:

- Long-term student memory
- Personalized learning profiles
- Multiple teaching strategies
- Retrieval-Augmented Generation (RAG)
- Subject-specific knowledge tools
- Teacher analytics dashboard
- Student progress tracking
- Personalized learning paths
- Multi-agent collaboration

---

## ⚠️ Disclaimer

ConfusionDetect is an educational prototype developed to demonstrate adaptive AI Agent concepts.

It is not intended to replace teachers or formal educational assessment.

---

## 👩‍💻 Author

**Nouf Aljabri**

Computer Science 