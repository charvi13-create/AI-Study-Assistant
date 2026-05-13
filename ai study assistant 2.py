import random
import time

score_history = []

#  FUNCTIONS 

def study_topic():
    topic = input("Enter topic you want to study: ")
    print("You are studying:", topic)


def take_quiz():
    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter your choice: ")

    # Questions WITH explanations
    easy = [
        ("What is 2 + 2 ?", "4", "2 + 2 = 4"),
        ("What is 5 + 1 ?", "6", "5 + 1 = 6"),
        ("What is 3 + 3 ?", "6", "3 + 3 = 6"),
        ("What is 4 + 4 ?", "8", "4 + 4 = 8")
    ]

    medium = [
        ("What is 12 - 5 ?", "7", "12 - 5 = 7"),
        ("What is 6 × 2 ?", "12", "6 × 2 = 12"),
        ("What is 15 ÷ 3 ?", "5", "15 ÷ 3 = 5"),
        ("What is 9 × 2 ?", "18", "9 × 2 = 18")
    ]

    hard = [
        ("What is 25 × 2 ?", "50", "25 × 2 = 50"),
        ("What is 100 ÷ 4 ?", "25", "100 ÷ 4 = 25"),
        ("What is 12 × 3 ?", "36", "12 × 3 = 36"),
        ("What is 50 ÷ 5 ?", "10", "50 ÷ 5 = 10")
    ]

    if level == "1":
        questions = easy
    elif level == "2":
        questions = medium
    elif level == "3":
        questions = hard
    else:
        print("Invalid level")
        return

    score = 0
    time_limit = 5

    random.shuffle(questions)

    # ✅ Quiz loop
    for q, ans, exp in questions[:3]:
        print("\nYou have", time_limit, "seconds!")

        start = time.time()
        answer = input(q + " ")
        end = time.time()

        if end - start > time_limit:
            print("⏰ Time's up!")
            print("Explanation:", exp)

        elif answer == ans:
            print("Correct!")
            score += 1

        else:
            print("Wrong answer")
            print("Explanation:", exp)

    # AFTER loop
    print("Your score is:", score, "/3")
    score_history.append(score)


# MAIN PROGRAM 

print("=== AI Study Assistant ===")

name = input("Enter your name: ")
subject = input("Which subject do you want to study? ")

print("\nHello", name)
print("Today we will study", subject)

# MENU LOOP 

while True:
    print("\n1. Study a topic")
    print("2. Take a quiz")
    print("3. View score history")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        study_topic()

    elif choice == "2":
        take_quiz()

    elif choice == "3":
        if len(score_history) == 0:
            print("No quiz attempts yet.")
        else:
            print("Your past scores:", score_history)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
