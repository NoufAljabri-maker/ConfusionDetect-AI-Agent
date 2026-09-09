import streamlit as st

from agent import (
    analyze_confusion,
    evaluate_answer
)

MAX_ATTEMPTS = 3

st.set_page_config(
    page_title="ConfusionDetect AI Agent",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 ConfusionDetect AI Agent")

st.caption(
    "An adaptive AI teaching agent that detects misconceptions, "
    "evaluates understanding, and changes its teaching strategy."
)

st.info(
    "Agent Flow: Diagnose → Ask → Evaluate → Adapt → Re-evaluate"
)

if "confusion" not in st.session_state:
    st.session_state.confusion = ""

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "attempt" not in st.session_state:
    st.session_state.attempt = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "completed" not in st.session_state:
    st.session_state.completed = False

if "status" not in st.session_state:
    st.session_state.status = "Waiting for student input"


st.subheader("1️⃣ Describe Your Confusion")

student_input = st.text_area(
    "What concept are you confused about?",
    placeholder=(
        "Example: I think RAM and hard disk are the same "
        "because both store data."
    ),
    height=120
)

if st.button("🚀 Start Agent", use_container_width=True):

    if student_input:

        st.session_state.confusion = student_input
        st.session_state.attempt = 0
        st.session_state.history = []
        st.session_state.completed = False
        st.session_state.status = "Diagnosing misconception"

        with st.spinner("Agent is diagnosing the misconception..."):

            st.session_state.analysis = analyze_confusion(
                student_input
            )

        st.session_state.status = "Waiting for diagnostic answer"

    else:

        st.warning("Please describe your confusion first.")


st.divider()

st.subheader("🤖 Agent Status")

st.write(f"**Current Status:** {st.session_state.status}")

if st.session_state.attempt > 0:
    st.progress(
        min(
            st.session_state.attempt / MAX_ATTEMPTS,
            1.0
        )
    )

if st.session_state.analysis:

    st.subheader("2️⃣ Initial Diagnosis")

    with st.container(border=True):
        st.write(st.session_state.analysis)


if (
    st.session_state.analysis
    and not st.session_state.completed
):

    st.subheader("3️⃣ Diagnostic Interaction")

    st.write(
        f"**Attempt {st.session_state.attempt + 1} "
        f"of {MAX_ATTEMPTS}**"
    )

    student_answer = st.text_area(
        "Answer the agent's latest question:",
        key=f"answer_{st.session_state.attempt}",
        height=100
    )

    if st.button(
        "🧪 Evaluate My Answer",
        key=f"submit_{st.session_state.attempt}",
        use_container_width=True
    ):

        if student_answer:

            st.session_state.status = "Evaluating understanding"
            st.session_state.attempt += 1

            with st.spinner(
                "Agent is evaluating your understanding..."
            ):

                evaluation = evaluate_answer(
                    st.session_state.confusion,
                    student_answer,
                    st.session_state.attempt
                )

            st.session_state.history.append(
                {
                    "attempt": st.session_state.attempt,
                    "answer": student_answer,
                    "evaluation": evaluation
                }
            )

            if (
                "UNDERSTOOD" in evaluation
                and
                "PARTIALLY_UNDERSTOOD"
                not in evaluation
            ):

                st.session_state.completed = True
                st.session_state.status = "Completed successfully"

            elif st.session_state.attempt >= MAX_ATTEMPTS:

                st.session_state.completed = True
                st.session_state.status = "Completed after maximum attempts"

            else:

                st.session_state.status = "Adapting teaching strategy"

            st.rerun()

        else:

            st.warning(
                "Please answer the diagnostic question first."
            )


if st.session_state.history:

    st.subheader("4️⃣ Agent Decision History")

    for item in st.session_state.history:

        with st.expander(
            f"Attempt {item['attempt']}"
        ):

            st.markdown("**Student Answer**")
            st.write(item["answer"])

            st.markdown("**Agent Decision**")
            st.write(item["evaluation"])


if st.session_state.completed:

    st.success("✅ Agent session completed.")

    st.write(
        f"The agent completed the session in "
        f"{st.session_state.attempt} attempt(s)."
    )


st.divider()

if st.button(
    "🔄 Start Over",
    use_container_width=True
):

    st.session_state.clear()
    st.rerun()


st.caption(
    "ConfusionDetect is an educational prototype. "
    "It is designed to demonstrate adaptive AI-agent behavior."
)