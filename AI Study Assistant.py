print(" AI Study Assistant ")

name = input("Enter your name: ")

subject = input("Which subject do you want to study? ")
print()
print("Hello", name)
print("Today we will study", subject)
print("Good luck!")
print("1. Study a topic")
print("2. Take a quiz")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
    topic = input("Enter topic you want to study: ")
    print("You are studying:", topic)

elif choice == "2":
    score = 0

    answer = input("What is 5 + 3 ? ")
    if answer == "8":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    answer = input("What is 10 - 4 ? ")
    if answer == "6":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    answer = input("What is 3 × 3 ? ")
    if answer == "9":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    print("Your score is:", score, "/3")

elif choice == "3":
    print("Goodbye!")

else:
    print("Invalid option")
print("=== AI Study Assistant ===")

name = input("Enter your name: ")
subject = input("Which subject do you want to study? ")

print("\nHello", name)
print("Today we will study", subject)

while True:
    print("\n1. Study a topic")
    print("2. Take a quiz")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        topic = input("Enter topic you want to study: ")
        print("You are studying:", topic)

    elif choice == "2":
        score = 0

        answer = input("What is 5 + 3 ? ")
        if answer == "8":
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")

        answer = input("What is 10 - 4 ? ")
        if answer == "6":
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")

        answer = input("What is 3 × 3 ? ")
        if answer == "9":
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")

        print("Your score is:", score, "/3")

    elif choice == "3":
        print("Goodbye!")
        break   

    else:
        print("Invalid option")
import random

def study_topic():
    topic = input("Enter topic you want to study: ")
    print("You are studying:", topic)


def take_quiz():
    score = 0

    answer = input("What is 5 + 3 ? ")
    if answer == "8":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    answer = input("What is 10 - 4 ? ")
    if answer == "6":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    answer = input("What is 3 × 3 ? ")
    if answer == "9":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

    print("Your score is:", score, "/3")


print("=== AI Study Assistant ===")

name = input("Enter your name: ")
subject = input("Which subject do you want to study? ")

print("\nHello", name)
print("Today we will study", subject)

#loop
while True:
    print("\n1. Study a topic")
    print("2. Take a quiz")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        study_topic()

    elif choice == "2":
        take_quiz()

    elif choice == "3":
        print("Goodbye!")
        break   

    else:
        print("Invalid option")
import random

def take_quiz():
    questions = [
        ("What is 5 + 3 ?", "8"),
        ("What is 10 - 4 ?", "6"),
        ("What is 3 × 3 ?", "9"),
        ("What is 7 + 2 ?", "9"),
        ("What is 6 ÷ 2 ?", "3")
    ]

    score = 0

    random.shuffle(questions)   

    for q, ans in questions[:3]:   
        answer = input(q + " ")

        if answer == ans:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")

    print("Your score is:", score, "/3")
