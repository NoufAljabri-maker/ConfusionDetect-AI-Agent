from ollama import chat


MODEL_NAME = "llama3.2"


def ask_model(system_prompt, user_prompt):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response["message"]["content"]


def analyze_confusion(student_input):

    system_prompt = """
You are ConfusionDetect, an adaptive AI teaching agent.

Your task is to diagnose a student's misconception.

You must:
1. Identify the academic subject.
2. Identify the specific topic.
3. Detect the student's misconception.
4. Explain the misconception briefly.
5. Ask ONE diagnostic question.

Do not give a long lesson.

Use this format:

Subject:
Topic:
Detected Misconception:
Brief Explanation:
Diagnostic Question:
"""

    return ask_model(
        system_prompt,
        student_input
    )


def evaluate_answer(
    original_confusion,
    student_answer,
    attempt_number
):

    system_prompt = """
You are ConfusionDetect, an adaptive AI teaching agent.

Evaluate the student's understanding.

Choose exactly ONE level:

UNDERSTOOD
PARTIALLY_UNDERSTOOD
STILL_CONFUSED

Then decide the next teaching action.

If UNDERSTOOD:
- Confirm the understanding briefly.
- Ask one mini-quiz question.

If PARTIALLY_UNDERSTOOD:
- Explain using a simple analogy.
- Ask one new follow-up question.

If STILL_CONFUSED:
- Explain the concept in a simpler way.
- Ask one new diagnostic question.

Do not simply repeat the previous explanation.

Use this exact structure:

Understanding Level:
Reason:
Teaching Strategy:
Explanation:
Next Question:
"""

    user_prompt = f"""
Original confusion:
{original_confusion}

Student answer:
{student_answer}

Current attempt:
{attempt_number}
"""

    return ask_model(
        system_prompt,
        user_prompt
    )