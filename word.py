import tkinter as tk
from tkinter import font, colorchooser, ttk

# Function to increase font size of selected text or entire text
# def increase_font_size():
#     try:
#         selected_range = text_widget.tag_ranges(tk.SEL)
#         if selected_range:
#             start, end = selected_range
#             current_font = font.nametofont(text_widget.tag_cget("sel", "font"))
#             current_size = current_font["size"]
#             new_size = current_size + 2
#             new_font = font.Font(family=current_font["family"], size=new_size)
#             text_widget.tag_add("font_increase", start, end)
#             text_widget.tag_configure("font_increase", font=new_font)
#         else:
#             current_font = font.nametofont(text_widget.cget("font"))
#             current_size = current_font["size"]
#             new_size = current_size + 2
#             new_font = font.Font(family=current_font["family"], size=new_size)
#             text_widget.config(font=new_font)
#     except tk.TclError:
#         pass

def increase_font_size():
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            # Get current font of the selected text
            current_font = font.nametofont(text_widget.tag_cget("sel", "font") if text_widget.tag_ranges(tk.SEL) else text_widget.cget("font"))
            current_size = current_font["size"]
            new_size = current_size + 2  # Increase font size
            new_font = font.Font(family=current_font["family"], size=new_size)
            # Apply the new font to the selected range
            text_widget.tag_add("font_increase", start, end)
            text_widget.tag_configure("font_increase", font=new_font)
        else:
            # If no text is selected, apply the font size change to the entire text
            current_font = font.nametofont(text_widget.cget("font"))
            current_size = current_font["size"]
            new_size = current_size + 2  # Increase font size
            new_font = font.Font(family=current_font["family"], size=new_size)
            text_widget.config(font=new_font)
    except tk.TclError:
        pass
# Function to decrease font size of selected text or entire text
def decrease_font_size():
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            current_font = font.nametofont(text_widget.tag_cget("sel", "font"))
            current_size = current_font["size"]
            new_size = current_size - 2
            new_font = font.Font(family=current_font["family"], size=new_size)
            text_widget.tag_add("font_decrease", start, end)
            text_widget.tag_configure("font_decrease", font=new_font)
        else:
            current_font = font.nametofont(text_widget.cget("font"))
            current_size = current_font["size"]
            new_size = current_size - 2
            new_font = font.Font(family=current_font["family"], size=new_size)
            text_widget.config(font=new_font)
    except tk.TclError:
        pass

# Function to change the font style of selected text
def change_font_style(event):
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            selected_font = font_style_var.get()
            text_widget.tag_add("font_style", start, end)
            text_widget.tag_configure("font_style", family=selected_font)
    except tk.TclError:
        pass

# Function to toggle bold for selected text
def toggle_bold():
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            current_weight = font.nametofont(text_widget.tag_cget("sel", "font"))["weight"]
            new_weight = "bold" if current_weight == "normal" else "normal"
            text_widget.tag_add("bold", start, end)
            text_widget.tag_configure("bold", weight=new_weight)
    except tk.TclError:
        pass

# Function to toggle italic for selected text
def toggle_italic():
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            current_slant = font.nametofont(text_widget.tag_cget("sel", "font"))["slant"]
            new_slant = "italic" if current_slant == "roman" else "roman"
            text_widget.tag_add("italic", start, end)
            text_widget.tag_configure("italic", slant=new_slant)
    except tk.TclError:
        pass

# Function to toggle underline for selected text
def toggle_underline():
    try:
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            current_underline = font.nametofont(text_widget.tag_cget("sel", "font"))["underline"]
            new_underline = 1 if current_underline == 0 else 0
            text_widget.tag_add("underline", start, end)
            text_widget.tag_configure("underline", underline=new_underline)
    except tk.TclError:
        pass

# Function to change the text color of selected text
def change_text_color():
    try:
        color = colorchooser.askcolor()[1]  # Get the selected color
        selected_range = text_widget.tag_ranges(tk.SEL)
        if selected_range:
            start, end = selected_range
            text_widget.tag_add("text_color", start, end)
            text_widget.tag_configure("text_color", foreground=color)
        else:
            text_widget.config(fg=color)
    except tk.TclError:
        pass

# Function to change the background color of the Text widget
def change_bg_color():
    color = colorchooser.askcolor()[1]
    text_widget.config(bg=color)

# Create main window
root = tk.Tk()
root.title("My Word Processor")

# Set the default font
text_font = font.Font(family="Arial", size=12)

# Create a Text widget for typing (dynamic resizing of container)
text_widget = tk.Text(root, wrap="word", font=text_font)
text_widget.pack(padx=10, pady=10, fill="both", expand=True)

# Create a toolbar frame
toolbar = tk.Frame(root)
toolbar.pack(fill="x")

# Font Size Controls (Increase/Decrease)
increase_button = tk.Button(toolbar, text="A+", command=increase_font_size)
increase_button.pack(side="left", padx=5)

decrease_button = tk.Button(toolbar, text="A-", command=decrease_font_size)
decrease_button.pack(side="left", padx=5)

# Font Style Dropdown
font_style_var = tk.StringVar()
font_style_dropdown = ttk.Combobox(toolbar, textvariable=font_style_var, values=["Arial", "Helvetica", "Times New Roman", "Courier", "Verdana"])
font_style_dropdown.set("Arial")
font_style_dropdown.bind("<<ComboboxSelected>>", change_font_style)
font_style_dropdown.pack(side="left", padx=5)

# Bold, Italic, Underline Buttons
bold_button = tk.Button(toolbar, text="B", font=("Arial", 10, "bold"), command=toggle_bold)
bold_button.pack(side="left", padx=5)

italic_button = tk.Button(toolbar, text="I", font=("Arial", 10, "italic"), command=toggle_italic)
italic_button.pack(side="left", padx=5)

underline_button = tk.Button(toolbar, text="U", font=("Arial", 10, "underline"), command=toggle_underline)
underline_button.pack(side="left", padx=5)

# Text Alignment Buttons
align_left_button = tk.Button(toolbar, text="Left", command=lambda: text_widget.tag_add("left", "1.0", "end"))
align_left_button.pack(side="left", padx=5)

align_center_button = tk.Button(toolbar, text="Center", command=lambda: text_widget.tag_add("center", "1.0", "end"))
align_center_button.pack(side="left", padx=5)

align_right_button = tk.Button(toolbar, text="Right", command=lambda: text_widget.tag_add("right", "1.0", "end"))
align_right_button.pack(side="left", padx=5)

# Text Color Button
text_color_button = tk.Button(toolbar, text="Text Color", command=change_text_color)
text_color_button.pack(side="left", padx=5)

# Background Color Button
bg_color_button = tk.Button(toolbar, text="BG Color", command=change_bg_color)
bg_color_button.pack(side="left", padx=5)

# Run the Tkinter event loop
root.mainloop()
