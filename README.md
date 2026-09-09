# 🧠 ConfusionDetect AI Agent

ConfusionDetect is an adaptive AI teaching agent that identifies student misconceptions, asks diagnostic questions, evaluates understanding, and changes its teaching strategy based on the student's responses.

The project is designed to clearly demonstrate the core behavior of an AI Agent:

**Observe → Diagnose → Ask → Evaluate → Decide → Adapt → Re-evaluate**

---

## 🚀 Project Idea

Traditional educational chatbots usually provide a direct answer to a student's question.

ConfusionDetect works differently.

Instead of immediately giving the answer, the agent:

1. Analyzes the student's statement.
2. Detects the possible misconception.
3. Identifies the academic subject and topic.
4. Asks a diagnostic question.
5. Evaluates the student's response.
6. Determines the student's understanding level.
7. Adapts its teaching strategy.
8. Repeats the process when needed.

---

## 🤖 Agent Workflow

```text
Student Input
      ↓
Misconception Detection
      ↓
Diagnostic Question
      ↓
Student Response
      ↓
Understanding Evaluation
      ↓
┌───────────────────────────┐
│ UNDERSTOOD                │
│ PARTIALLY_UNDERSTOOD      │
│ STILL_CONFUSED            │
└─────────────┬─────────────┘
              ↓
Adaptive Teaching Strategy
              ↓
New Question / Mini Quiz
              ↓
Re-evaluation