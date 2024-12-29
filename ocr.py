import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read the PDF: {e}")
        return ""


def summarize_text(text, num_sentences=3):
    """Summarize text using TF-IDF."""
    try:
        sentences = text.split('. ')
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(sentences)
        scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
        ranked_sentences = [sentences[i] for i in scores.argsort()[-num_sentences:][::-1]]
        return '. '.join(ranked_sentences)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to summarize text: {e}")
        return ""


def open_file():
    """Open a PDF file and extract content."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        extracted_text = extract_text_from_pdf(file_path)
        if extracted_text:
            summarized_content = summarize_text(extracted_text)
            summary_box.delete(1.0, tk.END)
            summary_box.insert(tk.END, summarized_content)
        else:
            summary_box.delete(1.0, tk.END)
            summary_box.insert(tk.END, "No content extracted from PDF.")


# Create the main window
root = tk.Tk()
root.title("PDF Summarizer")
root.geometry("800x600")
root.minsize(600, 400)  # Set a minimum size for the window

# Configure grid layout for full alignment
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Add title label
title_label = tk.Label(root, text="PDF Summarizer", font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Add file open button
open_button = tk.Button(root, text="Open PDF", command=open_file, font=("Arial", 14), bg="skyblue", fg="black")
open_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Add a container for the summary
summary_label = tk.Label(root, text="Summary:", font=("Arial", 14))
summary_label.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

summary_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
summary_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add a copy button
def copy_to_clipboard():
    """Copy summary to clipboard."""
    root.clipboard_clear()
    root.clipboard_append(summary_box.get(1.0, tk.END).strip())
    root.update()
    messagebox.showinfo("Success", "Summary copied to clipboard!")

copy_button = tk.Button(root, text="Copy Summary", command=copy_to_clipboard, font=("Arial", 14), bg="green", fg="white")
copy_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
