import streamlit as st

st.title("📖 Kids Bible Quiz")

questions = [
    {
        "question": "What is the first book of the Old Testament?",
        "options": ["Genesis", "Exodus", "Matthew", "Psalms"],
        "answer": "Genesis"
    },
    {
        "question": "Who built the ark?",
        "options": ["Moses", "Noah", "Abraham", "David"],
        "answer": "Noah"
    },
    {
        "question": "Who was swallowed by a big fish?",
        "options": ["Jonah", "Peter", "Paul", "Joseph"],
        "answer": "Jonah"
    }
]

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

# Current question
q = questions[st.session_state.index]

st.subheader(f"Question {st.session_state.index + 1} of {len(questions)}")
st.write(q["question"])

choice = st.radio("Choose an answer:", q["options"], key=st.session_state.index)

def check_answer(choice):
    try:
        if choice == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error("❌ Wrong!")
    except:
        st.warning("Please select an answer first.")

if st.button("Submit"):
    check_answer(choice)
    st.session_state.index += 1

# Quiz finished
if st.session_state.index >= len(questions):
    st.balloons()
    st.success(f"🎉 Quiz Finished! Your score: {st.session_state.score}/{len(questions)}")

    if st.button("Restart Quiz"):
        st.session_state.index = 0
        st.session_state.score = 0