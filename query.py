import tkinter as tk
from tkinter import messagebox

# Sample Questions and Answers
questions = [
    "What is the capital of France?",
    "Which programming language is known as 'Python'?",
    "What is 5 + 7?",
    "Which is the largest planet in our solar system?",
    "Who developed the theory of relativity?",
    "What is the boiling point of water?",
    "Which continent is the Sahara Desert located in?",
    "What is the chemical symbol for gold?",
    "Who painted the Mona Lisa?",
    "Which organ in the human body pumps blood?"
]

options = [
    ["Paris", "London", "Rome", "Berlin"],
    ["Java", "C++", "Python", "Ruby"],
    ["10", "11", "12", "13"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Newton", "Einstein", "Tesla", "Darwin"],
    ["90°C", "100°C", "110°C", "120°C"],
    ["Asia", "Africa", "Europe", "Australia"],
    ["Au", "Ag", "Fe", "Hg"],
    ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"],
    ["Heart", "Lungs", "Liver", "Kidneys"]
]

correct_answers = ["Paris", "Python", "12", "Jupiter", "Einstein", "100°C", "Africa", "Au", "Da Vinci", "Heart"]

# Application Logic
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Application")
        self.root.geometry("600x400")
        self.root.configure(bg="#E6F4F1")  # Light green background

        self.current_question = 0
        self.user_answers = [None] * len(questions)

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="#E6F4F1", wraplength=500)
        self.question_label.pack(pady=20)

        # Radio Buttons for options
        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12), bg="#E6F4F1")
            rb.pack(anchor="w", padx=50)
            self.options.append(rb)

        # Navigation Buttons
        self.nav_frame = tk.Frame(root, bg="#E6F4F1")
        self.nav_frame.pack(pady=20)

        self.prev_button = tk.Button(self.nav_frame, text="Previous", command=self.prev_question, bg="#4DB6AC", font=("Arial", 12), fg="white")
        self.prev_button.pack(side="left", padx=10)

        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.next_question, bg="#4DB6AC", font=("Arial", 12), fg="white")
        self.next_button.pack(side="left", padx=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit, bg="#00796B", font=("Arial", 14), fg="white")
        self.submit_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.question_label.config(text=f"Q{self.current_question + 1}: {questions[self.current_question]}")
        self.var.set(self.user_answers[self.current_question])  # Set previously selected answer
        for i, option in enumerate(options[self.current_question]):
            self.options[i].config(text=option, value=option)

    def save_answer(self):
        self.user_answers[self.current_question] = self.var.get()

    def prev_question(self):
        if self.current_question > 0:
            self.save_answer()
            self.current_question -= 1
            self.load_question()

    def next_question(self):
        if self.current_question < len(questions) - 1:
            self.save_answer()
            self.current_question += 1
            self.load_question()

    def submit(self):
        self.save_answer()
        if None in self.user_answers:
            messagebox.showwarning("Warning", "Please answer all the questions before submitting.")
            return
        score = sum(1 for i in range(len(questions)) if self.user_answers[i] == correct_answers[i])
        messagebox.showinfo("Result", f"You scored {score}/{len(questions)}")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
