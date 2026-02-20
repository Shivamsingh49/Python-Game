# Kaun Banega Crorepati Quiz Game
print("Welcome to Kaun Banega Crorepati")
print("Let's start the game!\n")

# Define questions, options, and answers
questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Butwal", "B. Narayanghat", "C. Kathmandu", "D. Bhaktpur"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of the Nepal?",
        "options": ["A. BhanuBhakt", "B. Prithvi narayan", "C. Kali Das", "D. Sanduk"],
        "answer": "B"
    },
    {
        "question": "How many disticks are there in Nepal?",
        "options": ["A. 50", "B. 70", "C. 100", "D. 77"],
        "answer": "D"
    },
    {
        "question": "Who wrote the Nepali National Anthem?",
        "options": ["A. Pradeep Kumar Rai", "B. Bankim Chandra", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
        "answer": "A"
    }
]

# Initial prize money
prize_money = [1000, 5000, 10000, 50000]
current_prize = 0

# Start asking questions
# i: The index of the current question(0, 1, 2, ....)
# q: The actual dictionary containing the question, options and answer.
for i, q in enumerate(questions):
    print(f"Question {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)
    
    # Get user input
    answer = input("Enter your answer (A, B, C, or D): ").upper()

    # Check if the answer is correct
    if answer == q['answer']:
        print("Correct Answer!")
        current_prize = prize_money[i]
        print(f"You have won Rs.{current_prize}!\n")
    else:
        print(" Wrong Answer! Better luck next time!")
        break

# Game Over
print(f"You are taking home Rs.{current_prize}. Thanks for playing Kaun Banega Crorepati!")
