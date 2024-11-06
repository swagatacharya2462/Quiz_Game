questions = [
    {
        "prompt": "What is the capital of India?",
        "options": ["A. Delhi", "B. Kolkata", "C. Mumbai", "D. Chennai"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. Hindi"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote the Ramayana?",
        "options": ["A. Valmiki", "B. Ved Vyas", "C. Tulsidas", "D. Kalidasa"],
        "answer": "A"
    }
]


def run_quiz(questions):
    score = 0
    print("Welcome to the Quiz! Answer each question by selecting the correct option (A, B, C, or D).")
    print("=" * 50)

    for index, question in enumerate(questions, start=1):
        print(f"Question {index}: {question['prompt']}")
        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A, B, C, or D): ").upper()
            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")

        print("=" * 50)

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")


run_quiz(questions)
