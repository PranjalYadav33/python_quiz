# app.py
import streamlit as st
import random
import time

# --- ASCII Art Definitions (Upgraded for Better Aesthetics) ---

HEADER_ART = """
 ____        _   _                 ____        _     __  __ 
|  _ \ _   _| |_| |__   ___  _ __ / ___| _   _(_)___|  \/  |
| |_) | | | | __| '_ \ / _ \| '_ \\___ \| | | | / __| |\/| |
|  __/| |_| | |_| | | | (_) | | | |___) | |_| | \__ \ |  | |
|_|    \__, |\__|_| |_|\___/|_| |_|____/ \__,_|_|___/_|  |_|
       |___/                                               
       
        ...
       / o o \\
       \  ---  /
        \_____/
       /  ---  \\
      /         \\
     |           |
     |           |
"""

CORRECT_ART = """
      *******************
      *                 *
      *     CORRECT!    *
      *                 *
      *******************
          \\   ^__^
           \\  (oo)\\_______
              (__)\\       )\\/\\
                  ||----w |
                  ||     ||
"""

WRONG_ART = """
      *******************
      *                 *
      *    INCORRECT    *
      *                 *
      *******************
         /     \\
        /       \\
        |  O O  |
        |   >   |
        \\  ---  /
         \\_____/
"""

TROPHY_ART = """
      '._==_==_=_.'
      .-\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\::.    /
         '::. .'
           ) (
         _.' '._
        `-------`
  C O N G R A T U L A T I O N S !
"""

# --- Your List of Questions ---
questions = [
    {
        "prompt": "What keyword is used to create a function in Python?",
        "options": ["A. def", "B. function", "C. fun", "D. define"],
        "answer": "A"
    },
    {
        "prompt": "Which data type is used to store a sequence of characters?",
        "options": ["A. int", "B. str", "C. list", "D. char"],
        "answer": "B"
    },
    {
        "prompt": "How do you get the number of items in a list named 'my_list'?",
        "options": ["A. my_list.size()", "B. len(my_list)", "C. my_list.length", "D. count(my_list)"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following is the 'not equal to' operator?",
        "options": ["A. =!", "B. <>", "C. !=", "D. =="],
        "answer": "C"
    },
    {
        "prompt": "How do you access the value associated with the key 'name' in a dictionary called 'person'?",
        "options": ["A. person.get('name')", "B. person['name']", "C. person.value('name')", "D. Both A and B are correct"],
        "answer": "D"
    },
    {
        "prompt": "What is the correct way to start a single-line comment in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "prompt": "Which data structure is immutable, meaning it cannot be changed after creation?",
        "options": ["A. list", "B. dictionary", "C. set", "D. tuple"],
        "answer": "D"
    },
    {
        "prompt": "What will `my_list[0]` return for the list `my_list = ['a', 'b', 'c']`?",
        "options": ["A. 'a'", "B. 'b'", "C. ('a', 'b')", "D. An error"],
        "answer": "A"
    },
    {
        "prompt": "Which keyword is used to exit a loop prematurely?",
        "options": ["A. stop", "B. exit", "C. break", "D. continue"],
        "answer": "C"
    },
    {
        "prompt": "What is the output of `type(15.0)`?",
        "options": ["A. <class 'int'>", "B. <class 'str'>", "C. <class 'float'>", "D. <class 'number'>"],
        "answer": "C"
    },
    {
        "prompt": "How do you add the item `5` to the end of a list called `nums`?",
        "options": ["A. nums.add(5)", "B. nums.push(5)", "C. nums.append(5)", "D. nums.insert(5)"],
        "answer": "C"
    },
    {
        "prompt": "What keyword is used to bring a module's functions into your current script?",
        "options": ["A. include", "B. import", "C. load", "D. use"],
        "answer": "B"
    }
]

# --- Initialize Session State ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
if 'questions_asked' not in st.session_state:
    st.session_state.questions_asked = []
if 'quiz' not in st.session_state:
    st.session_state.quiz = None

# --- App Layout ---
st.title("Welcome to the...")
st.code(HEADER_ART, language=None)

# --- Quiz Logic ---
if st.session_state.question_num < 10:

    if st.session_state.quiz is None or st.session_state.quiz['prompt'] in st.session_state.questions_asked:
        available_questions = [q for q in questions if q['prompt'] not in st.session_state.questions_asked]
        if available_questions:
            st.session_state.quiz = random.choice(available_questions)
        else:
            st.session_state.question_num = 10 

    st.header(f"Question {st.session_state.question_num + 1} of 10")
    st.subheader(st.session_state.quiz['prompt'])

    # --- CHANGE 1: Use the full options directly. No more splitting. ---
    options = st.session_state.quiz['options']
    user_choice = st.radio("Choose your answer:", options, index=None)

    if st.button("Submit Answer", type="primary"):
        if user_choice:
            # --- CHANGE 2: Get the letter directly from the user's choice. ---
            # This is now simple and bug-free.
            user_answer_letter = user_choice.split('.')[0]

            if user_answer_letter == st.session_state.quiz['answer']:
                st.balloons()
                st.code(CORRECT_ART, language=None)
                st.session_state.score += 1
            else:
                st.error(f"Not quite! The correct answer was {st.session_state.quiz['answer']}.")
                st.code(WRONG_ART, language=None)
            
            st.session_state.questions_asked.append(st.session_state.quiz['prompt'])
            st.session_state.question_num += 1
            time.sleep(2) 
            st.rerun()
        else:
            st.warning("Please select an answer before submitting.")

else:
    st.balloons()
    st.header("🎉 Quiz Complete! 🎉")
    st.code(TROPHY_ART, language=None)
    st.write(f"### Your final score is: **{st.session_state.score} out of 10**")
    
    if st.button("Play Again"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()