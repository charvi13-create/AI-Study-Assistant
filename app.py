import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

score_history = []

topics_data = {

    "programming": {
        "Variables":
            "Variables store data values.\n\n"
            "Example:\n x = 10\n name = 'Charvi'",

        "Loops":
            "Loops repeat code multiple times.\n\n"
            "Example:\n for i in range(5):\n     print(i)",

        "Functions":
            "Functions are reusable blocks of code.\n\n"
            "Defined using 'def'.",

        "OOP":
            "Object Oriented Programming uses classes and objects."
    },

    "data structures": {
        "Array":
            "Array stores multiple values using indexes.",

        "Stack":
            "Stack follows LIFO (Last In First Out).",

        "Queue":
            "Queue follows FIFO (First In First Out).",

        "Linked List":
            "Linked List uses connected nodes."
    },

    "dbms": {
        "Database":
            "Database stores organized data.",

        "SQL":
            "SQL is used to interact with databases.",

        "Normalization":
            "Normalization reduces redundancy.",

        "Primary Key":
            "Primary key uniquely identifies records."
    },

    "maths": {
        "Algebra":
            "Algebra deals with equations and variables.",

        "Calculus":
            "Calculus studies change and motion.",

        "Matrices":
            "Matrices are 2D arrangements of numbers.",

        "Trigonometry":
            "Trigonometry studies angles and triangles."
    },

    "english": {
        "Grammar":
            "Grammar is the set of language rules.",

        "Tenses":
            "Tenses show time of action.",

        "Vocabulary":
            "Vocabulary means words you know and use.",

        "Comprehension":
            "Comprehension means understanding text."
    }
}

root = tk.Tk()
root.title("Smart AI Study Assistant")
root.geometry("500x450")
root.configure(bg="#dbeafe")

def study_topic():

    subject = simpledialog.askstring(
        "Subject",
        "Enter subject:\nProgramming / Data Structures / DBMS / Maths / English"
    )

    if subject is None:
        return

    subject = subject.strip().lower()

    if subject not in topics_data:
        messagebox.showinfo("Error", "Subject not found!")
        return

    topics = list(topics_data[subject].keys())

    topic = simpledialog.askstring(
        "Topic",
        f"Available Topics:\n\n{', '.join(topics)}\n\nEnter topic:"
    )

    if topic is None:
        return

    topic = topic.strip().lower()

    found = False

    for t in topics_data[subject]:

        if topic == t.lower():

            explanation = topics_data[subject][t]

            messagebox.showinfo(
                t,
                f"📘 {t}\n\n{explanation}"
            )

            found = True
            break

    if not found:
        messagebox.showinfo(
            "Error",
            f"Topic not found!\nAvailable Topics:\n{', '.join(topics)}"
        )



def take_quiz():

    subject = simpledialog.askstring(
        "Subject",
        "Enter subject for quiz:"
    )

    if subject is None:
        return

    subject = subject.strip().lower()

    quiz_data = {

        "programming": {
            "easy": [
                ("Which keyword defines a function?", "def"),
                ("Which symbol is used for comments?", "#"),
                ("Which loop repeats code?", "for")
            ],

            "medium": [
                ("Which function takes input?", "input"),
                ("Which keyword creates class?", "class"),
                ("What does len('hi') return?", "2")
            ],

            "hard": [
                ("What does OOP stand for?", "object oriented programming"),
                ("Which data type stores text?", "string"),
                ("What is used to repeat code?", "loop")
            ]
        },

        "data structures": {
            "easy": [
                ("Which structure uses LIFO?", "stack"),
                ("Which structure uses FIFO?", "queue"),
                ("Which DS uses nodes?", "linked list")
            ],

            "medium": [
                ("Stack remove operation?", "pop"),
                ("Queue add operation?", "enqueue"),
                ("Top of stack?", "peek")
            ],

            "hard": [
                ("Array search type?", "linear"),
                ("Which DS uses pointers?", "linked list"),
                ("Queue remove operation?", "dequeue")
            ]
        },

        "dbms": {
            "easy": [
                ("DBMS stands for?", "database management system"),
                ("Which language is used in DBMS?", "sql"),
                ("Database stores?", "data")
            ],

            "medium": [
                ("Primary key is?", "unique"),
                ("Normalization reduces?", "redundancy"),
                ("SQL command to view data?", "select")
            ],

            "hard": [
                ("Foreign key creates?", "relationship"),
                ("Can primary key be null?", "no"),
                ("INSERT is used to?", "add")
            ]
        },

        "maths": {
            "easy": [
                ("2 + 2 ?", "4"),
                ("5 × 2 ?", "10"),
                ("10 ÷ 2 ?", "5")
            ],

            "medium": [
                ("sin(90)?", "1"),
                ("cos(0)?", "1"),
                ("tan(45)?", "1")
            ],

            "hard": [
                ("Derivative of x²?", "2x"),
                ("Integration of 1 dx?", "x"),
                ("Matrix is?", "2d array")
            ]
        },

        "english": {
            "easy": [
                ("Plural of book?", "books"),
                ("Which is a verb: run or table?", "run"),
                ("Opposite of big?", "small")
            ],

            "medium": [
                ("Past tense of go?", "went"),
                ("Synonym of happy?", "joyful"),
                ("Pronoun replaces?", "noun")
            ],

            "hard": [
                ("Adjective describes?", "noun"),
                ("Present tense example?", "i eat"),
                ("Vocabulary means?", "words")
            ]
        }
    }

    if subject not in quiz_data:
        messagebox.showinfo("Error", "Subject not available!")
        return

    level = simpledialog.askstring(
        "Difficulty",
        "Choose level:\nEasy / Medium / Hard"
    )

    if level is None:
        return

    level = level.strip().lower()

    if level not in quiz_data[subject]:
        messagebox.showerror("Error", "Invalid level!")
        return

    questions = quiz_data[subject][level]

    score = 0

    random.shuffle(questions)

    # Quiz loop
    for q, ans in questions:

        messagebox.showinfo(
            "Timer",
            "⏰ You have 10 seconds!"
        )

        start = time.time()

        answer = simpledialog.askstring(
            "Quiz",
            q
        )

        end = time.time()

        if answer is None:
            return

        if end - start > 10:
            messagebox.showinfo(
                "Time's Up!",
                "⏰ You took too long!"
            )
            continue

        if answer.strip().lower() == ans.lower():
            messagebox.showinfo(
                "Result",
                "✅ Correct!"
            )
            score += 1

        else:
            messagebox.showinfo(
                "Result",
                f"❌ Wrong!\nCorrect answer: {ans}"
            )

    # Final Feedback
    if score == len(questions):
        feedback = "Excellent! 🎉"

    elif score >= 2:
        feedback = "Good Job 👍"

    else:
        feedback = "Keep Practicing 💪"

    messagebox.showinfo(
        "Final Score",
        f"Your score is {score}/{len(questions)}\n\n{feedback}"
    )

    score_history.append(
        f"{subject} → {score}/{len(questions)}"
    )


def show_history():

    if len(score_history) == 0:

        messagebox.showinfo(
            "History",
            "No quiz attempts yet."
        )

    else:

        messagebox.showinfo(
            "History",
            f"Past Scores:\n\n" + "\n".join(score_history)
        )

label = tk.Label(
    root,
    text="Smart AI Study Assistant",
    font=("Arial", 18, "bold"),
    bg="#dbeafe"
)

label.pack(pady=20)

welcome = tk.Label(
    root,
    text="Learn • Practice • Improve",
    font=("Arial", 11),
    bg="#dbeafe"
)

welcome.pack()

study_btn = tk.Button(
    root,
    text="Study Topic",
    font=("Arial", 12),
    bg="#60a5fa",
    fg="white",
    width=20,
    command=study_topic
)

study_btn.pack(pady=10)

quiz_btn = tk.Button(
    root,
    text="Take Quiz",
    font=("Arial", 12),
    bg="#34d399",
    fg="white",
    width=20,
    command=take_quiz
)

quiz_btn.pack(pady=10)

history_btn = tk.Button(
    root,
    text="View Score History",
    font=("Arial", 12),
    bg="#f59e0b",
    fg="white",
    width=20,
    command=show_history
)

history_btn.pack(pady=10)

# =========================
# RUN APP
# =========================

root.mainloop()
