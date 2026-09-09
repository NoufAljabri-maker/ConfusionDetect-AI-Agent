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
