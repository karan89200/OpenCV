import tkinter as tk
from tkinter import messagebox

# Function to create MCQs from the provided story text (you can customize this part later for more advanced logic)
def generate_mcqs_from_story(story):
    # This is a basic example of how we might generate questions from a story
    questions = [
        "What is the main theme of the story?",
        "Who is the protagonist of the story?",
        "Where does the story take place?",
        "What is the conflict in the story?",
        "How does the story end?"
    ]
    
    # Option choices for each question (for simplicity, we assume they are predefined)
    options = [
        ["Love", "Adventure", "Betrayal", "Friendship"],  # for 'theme'
        ["John", "Alice", "Bob", "Charlie"],  # for 'protagonist'
        ["New York", "Paris", "London", "Tokyo"],  # for 'location'
        ["Betrayal", "Death", "Revenge", "Resolution"],  # for 'conflict'
        ["Happy", "Sad", "Cliffhanger", "Open-ended"]  # for 'ending'
    ]
    
    # Correct answers for the questions
    correct_answers = ["Adventure", "Alice", "Paris", "Betrayal", "Happy"]
    
    return questions, options, correct_answers

# Global Variables
current_question = 0
user_answers = [None] * 5
score = 0

# Create main window
root = tk.Tk()
root.title("MCQ Quiz from Story")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Function to apply gradient color to background
def apply_gradient(widget, color1, color2):
    widget.config(bg=color1)
    widget.after(0, lambda: widget.config(bg=color2))

# Story input window
def submit_story():
    global questions, options, correct_answers
    story_text = story_entry.get("1.0", tk.END).strip()
    
    if not story_text:
        messagebox.showwarning("Input Error", "Please provide a story.")
        return
    
    # Generate MCQs from the provided story
    questions, options, correct_answers = generate_mcqs_from_story(story_text)
    
    # Start the quiz after generating questions
    show_question()

# Function to calculate and show results
def submit():
    global score
    score = 0
    for idx, answer in enumerate(user_answers):
        if answer == correct_answers[idx]:
            score += 1

    # Show the score in a messagebox
    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(questions)}")
    show_results()

# Function to show the results
def show_results():
    global current_question
    current_question = 0

    # Clear the main window and show results
    for widget in root.winfo_children():
        widget.destroy()

    result_label = tk.Label(root, text="Results", font=("Helvetica", 24), fg="white", bg="#333")
    result_label.pack(pady=20)

    for i in range(len(questions)):
        question_frame = tk.Frame(root, bg="#f0f0f0")
        question_frame.pack(fill="x", padx=20, pady=10)

        # Question label
        question_label = tk.Label(question_frame, text=f"Q{i+1}: {questions[i]}", font=("Helvetica", 12), bg="#f0f0f0")
        question_label.pack(anchor="w")

        # Display options with colors
        for option in options[i]:
            color = "green" if option == correct_answers[i] else "red" if option == user_answers[i] else "black"
            option_label = tk.Label(question_frame, text=option, font=("Helvetica", 10), fg=color, bg="#f0f0f0")
            option_label.pack(anchor="w")

    retry_button = tk.Button(root, text="Retry", command=retry, bg="lightgreen", font=("Helvetica", 12), relief="flat")
    retry_button.pack(pady=20)

# Function to retry the quiz
def retry():
    global current_question, user_answers
    current_question = 0
    user_answers = [None] * len(questions)
    provide_story()

# Function to show the current question
def show_question():
    global current_question

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    question_label = tk.Label(root, text=f"Q{current_question + 1}: {questions[current_question]}", font=("Helvetica", 16), fg="white", bg="#333")
    question_label.pack(pady=20)

    # Create radio buttons for options
    var = tk.StringVar(value=user_answers[current_question])
    for option in options[current_question]:
        option_button = tk.Radiobutton(root, text=option, variable=var, value=option, font=("Helvetica", 12), fg="black", bg="#f0f0f0", command=lambda: set_answer(var.get()))
        option_button.pack(anchor="w")

    # Navigation buttons (Previous, Next, Submit)
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=20)

    if current_question > 0:
        prev_button = tk.Button(button_frame, text="Previous", command=previous_question, bg="lightblue", font=("Helvetica", 12), relief="flat")
        prev_button.grid(row=0, column=0, padx=10)

    if current_question < len(questions) - 1:
        next_button = tk.Button(button_frame, text="Next", command=next_question, bg="lightblue", font=("Helvetica", 12), relief="flat")
        next_button.grid(row=0, column=1, padx=10)
    else:
        submit_button = tk.Button(button_frame, text="Submit", command=submit, bg="lightgreen", font=("Helvetica", 12), relief="flat")
        submit_button.grid(row=0, column=1, padx=10)

# Function to set the answer for the current question
def set_answer(answer):
    global user_answers
    user_answers[current_question] = answer

# Navigate to the next question
def next_question():
    global current_question
    current_question += 1
    show_question()

# Navigate to the previous question
def previous_question():
    global current_question
    current_question -= 1
    show_question()

# Main window where user provides a story
def provide_story():
    for widget in root.winfo_children():
        widget.destroy()

    title_label = tk.Label(root, text="Enter the Story", font=("Helvetica", 20), fg="white", bg="#333")
    title_label.pack(pady=20)

    story_label = tk.Label(root, text="Story (Text Form):", font=("Helvetica", 12), fg="white", bg="#333")
    story_label.pack(anchor="w", padx=20)

    # Text box for story input
    global story_entry
    story_entry = tk.Text(root, height=10, width=60, font=("Helvetica", 12), relief="flat")
    story_entry.pack(pady=10)

    submit_story_button = tk.Button(root, text="Submit Story", command=submit_story, bg="lightblue", font=("Helvetica", 12), relief="flat")
    submit_story_button.pack(pady=20)

# Start by asking the user to enter the story
provide_story()

# Apply gradient effects to the window background
apply_gradient(root, "#4e73df", "#1c61b3")

# Run the Tkinter event loop
root.mainloop()
