import random
import time

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

print("======== Want to Take a Test? Take a Quiz! ========")
print()

score = 0
num_questions_to_ask = 10

start_time = time.time()

for question_num in range(num_questions_to_ask):
    
    quiz = random.choice(questions)

    print(f"===== Question {question_num + 1} of {num_questions_to_ask} =====")
    print()
    print(quiz["prompt"])
    print()

    for option in quiz["options"]:
        print(option)
    
    print()

    check_answer = input("Select one answer from the options (A, B, C, D): ").upper()

    if check_answer == quiz["answer"]:
        score += 1
        print(f"'{check_answer}' is the correct answer.")
        print()
    else:
        print(f"'{check_answer}' is the wrong answer. The correct answer was {quiz['answer']}.")
        print()

    questions.remove(quiz)

end_time = time.time()

total_time = end_time - start_time

print("====================================")
print(f"Quiz Complete! You got {score} out of {num_questions_to_ask}.")
print(f"Total time taken: {total_time:.2f} seconds.")
print("====================================")
