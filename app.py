import tkinter as tk
from tkinter import simpledialog, messagebox
import random
score_history = []


topics_data = {

    "programming": {
        "Variables":
            "Variables are used to store data values in a program.\n\n"
            "Example:\n x = 10\n name = 'Charvi'\n\n"
            "They allow us to reuse and manipulate data easily.",

        "Loops":
            "Loops are used to repeat a block of code multiple times.\n\n"
            "Types:\n- for loop\n- while loop\n\n"
            "Example:\n for i in range(5):\n     print(i)\n\n"
            "This prints numbers from 0 to 4.",

        "Functions":
            "Functions are reusable blocks of code.\n\n"
            "Defined using 'def'.\n\n"
            "Example:\n def add(a, b):\n     return a + b\n\n"
            "They help reduce repetition and organize code.",

        "OOP":
            "Object Oriented Programming organizes code using classes and objects.\n\n"
            "Example:\n class Student:\n     pass\n\n"
            "It helps in building scalable applications."
    },

    "data structures": {
        "Array":
            "An array stores multiple elements in a single structure.\n\n"
            "Example:\n arr = [1, 2, 3]\n\n"
            "Each element is accessed using an index.",

        "Stack":
            "Stack follows LIFO (Last In First Out).\n\n"
            "Operations:\n- push\n- pop\n\n"
            "Example:\nPush 1, Push 2 → Pop removes 2.",

        "Queue":
            "Queue follows FIFO (First In First Out).\n\n"
            "Operations:\n- enqueue\n- dequeue\n\n"
            "Example:\nAdd 1, Add 2 → Remove removes 1.",

        "Linked List":
            "A linked list consists of nodes connected using pointers.\n\n"
            "Each node contains data and a link to next node.\n\n"
            "Used in dynamic memory allocation."
    },

    "dbms": {
        "Database":
            "A database is an organized collection of data.\n\n"
            "Example:\nStudent records in a system.\n\n"
            "It helps store and manage data efficiently.",

        "SQL":
            "SQL is used to interact with databases.\n\n"
            "Commands:\n- SELECT\n- INSERT\n- DELETE\n\n"
            "Example:\nSELECT * FROM students;",

        "Normalization":
            "Normalization reduces data redundancy.\n\n"
            "It organizes data into proper tables.\n\n"
            "Improves efficiency and avoids duplication.",

        "Primary Key":
            "Primary key uniquely identifies each record.\n\n"
            "Example:\nStudent ID.\n\n"
            "Cannot be null or duplicate.",

        "Foreign Key":
            "Foreign key connects two tables.\n\n"
            "It creates relationships between data.\n\n"
            "Example:\nStudent ID referencing another table."
    },

    "maths": {
        "Algebra":
            "Algebra deals with variables and equations.\n\n"
            "Example:\n x + 2 = 5 → x = 3\n\n"
            "Used to find unknown values.",

        "Calculus":
            "Calculus studies change and motion.\n\n"
            "Includes differentiation and integration.\n\n"
            "Used in engineering and physics.",

        "Matrices":
            "A matrix is a 2D arrangement of numbers.\n\n"
            "Example:\n [1 2]\n [3 4]\n\n"
            "Used to solve systems of equations.",

        "Trigonometry":
            "Trigonometry studies angles and triangles.\n\n"
            "Important:\n sin, cos, tan\n\n"
            "Example:\n sin(90°) = 1"
    },

    "english": {
        "Grammar":
            "Grammar is the system of rules in a language.\n\n"
            "Includes nouns, verbs, tenses.\n\n"
            "Example:\nShe is going to school.",

        "Tenses":
            "Tenses show time of action.\n\n"
            "Present, Past, Future.\n\n"
            "Example:\nI eat / I ate / I will eat.",

        "Vocabulary":
            "Vocabulary is the set of words you know.\n\n"
            "Example:\nHappy → Joyful\nBig → Large\n\n"
            "Improves communication skills.",

        "Comprehension":
            "Comprehension means understanding text.\n\n"
            "It helps in reading and answering questions correctly."
    },
}
# create window
root = tk.Tk()
root.title("AI Study Assistant")
root.geometry("500x400")

# function for study topic
def study_topic():
    subject = simpledialog.askstring("Subject", "Enter subject:")

    if subject is None:
        return

    subject = subject.strip().lower()

    if subject not in topics_data:
        messagebox.showinfo("Error", "Subject not found!")
        return

    topics = list(topics_data[subject].keys())

    topic = simpledialog.askstring(
        "Topic",
        f"Available topics:\n{', '.join(topics)}\n\nEnter one:"
    )

    if topic is None:
        return

    topic = topic.strip().lower()

    found = False

    for t in topics_data[subject]:
        if topic == t.lower():
            explanation = topics_data[subject][t]
            messagebox.showinfo(t, explanation)
            found = True
            break

    if not found:
        messagebox.showinfo("Error", "Topic not found!")
def take_quiz():
    subject = simpledialog.askstring("Subject", "Enter subject for quiz:")

    if subject is None:
        return

    subject = subject.strip().lower()

    # ALL SUBJECT QUIZ DATA IN ONE PLACE
    quiz_data = {

        "programming": {
            "easy": [
                ("Which keyword defines a function?", "def"),
                ("Which symbol is used for comments?", "#"),
                ("Which loop repeats code?", "for")
            ],
            "medium": [
                ("What is the output of 2+2?", "4"),
                ("Which data type stores text?", "string"),
                ("What does len('hi') return?", "2")
            ],
            "hard": [
                ("What does OOP stand for?", "object oriented programming"),
                ("Which function takes input?", "input"),
                ("Which keyword defines class?", "class")
            ]
        },

        "data structures": {
            "easy": [
                ("Which structure uses LIFO?", "stack"),
                ("Which uses FIFO?", "queue"),
                ("Array stores how many elements?", "multiple")
            ],
            "medium": [
                ("Stack remove operation?", "pop"),
                ("Queue add operation?", "enqueue"),
                ("Which DS uses nodes?", "linked list")
            ],
            "hard": [
                ("Top of stack is called?", "peek"),
                ("Which DS uses pointers?", "linked list"),
                ("Search time in array?", "linear")
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
                ("Foreign key is used for?", "relationship"),
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
                ("Derivative of x^2?", "2x"),
                ("Value of sin(90)?", "1"),
                ("Matrix is?", "2d array")
            ],
            "hard": [
                ("Integration of 1 dx?", "x"),
                ("cos(0)?", "1"),
                ("tan(45)?", "1")
            ]
        },

        "english": {
            "easy": [
                ("Plural of book?", "books"),
                ("Which is a verb: run or table?", "run"),
                ("Noun means?", "name")
            ],
            "medium": [
                ("Opposite of big?", "small"),
                ("Synonym of happy?", "joyful"),
                ("'I am eating' tense?", "present")
            ],
            "hard": [
                ("Past tense of go?", "went"),
                ("Pronoun replaces?", "noun"),
                ("Adjective describes?", "noun")
            ]
        }
    }

    #  Subject check
    if subject not in quiz_data:
        messagebox.showinfo("Error", "Subject not available!")
        return

    #  Difficulty
    level = simpledialog.askstring("Difficulty", "Choose level: Easy / Medium / Hard")

    if level is None:
        return

    level = level.strip().lower()

    if level not in quiz_data[subject]:
        messagebox.showerror("Error", "Invalid level!")
        return

    questions = quiz_data[subject][level]

    score = 0
    random.shuffle(questions)

    #  Quiz loop
    for q, ans in questions:
        messagebox.showinfo("Timer", "You have 10 seconds!")

        start = time.time()
        answer = simpledialog.askstring("Quiz", q)
        end = time.time()

        if answer is None:
            return

        if end - start > 10:
            messagebox.showinfo("Time's up!", "⏰ You took too long!")
            continue

        if answer.strip().lower() == ans.lower():
            messagebox.showinfo("Result", "Correct!")
            score += 1
        else:
            messagebox.showinfo("Result", f"Wrong! Correct answer is {ans}")
    #  Final score
    if score == len(questions):
     feedback = "Excellent! 🎉"
    elif score >= 2:
     feedback = "Good job 👍"
    else:
     feedback = "Keep practicing 💪"

messagebox.showinfo("Final Score", f"Your score is {score}/{len(questions)}\n{feedback}")
score_history.append(f"{subject} → {score}/{len(questions)}")

def show_history():
    if len(score_history) == 0:
        messagebox.showinfo("History", "No quiz attempts yet.")
    else:
        messagebox.showinfo("History", f"Past scores: {score_history}")
# title label
label = tk.Label(root, text="AI Study Assistant", font=("Arial", 16))
label.pack(pady=20)
welcome = tk.Label(root, text="Learn • Practice • Improve", font=("Arial", 10))
welcome.pack()

# study button
study_btn = tk.Button(root, text="Study Topic", command=study_topic)
study_btn.pack(pady=10)

quiz_btn = tk.Button(root, text="Take Quiz", command=take_quiz)
quiz_btn.pack(pady=10)

history_btn = tk.Button(root, text="View Score History", command=show_history)
history_btn.pack(pady=10)

# run app
root.mainloop()
