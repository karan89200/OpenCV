import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Create the main window
root = tk.Tk()
root.title("Pixabay Image Viewer")

# Initialize variables
current_page = 1
images = []  # List to store image references
api_key = '47881300-3c75ef1624b700ed83f623e8c'  # Replace with your actual Pixabay API key

# Create a canvas and scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame for the images inside the canvas
image_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=image_frame, anchor="nw")

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Function to fetch images from the Pixabay API
def fetch_images(query, page):
    url = f"https://pixabay.com/api/?key={api_key}&q={query}&image_type=photo&page={page}&per_page=5"
    response = requests.get(url)
    data = response.json()

    if 'hits' not in data:
        messagebox.showerror("Error", "No images found!")
        return []

    new_images = []
    for hit in data['hits']:
        img_url = hit['webformatURL']
        img_response = requests.get(img_url)
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200))  # Resize to standard display size
        new_images.append(img)
    
    return new_images

# Function to update the image display
def update_images():
    global images
    row = tk.Frame(image_frame)  # Create a new row (frame for images)
    
    # Add images to the row
    for i, img in enumerate(images):
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(row, image=img_tk)
        label.image = img_tk
        label.pack(side=tk.LEFT, padx=5, pady=5)  # Pack images horizontally

        # Bind the label to show the larger image when clicked
        label.bind("<Button-1>", lambda event, img=img: show_large_image(event, img))
    
    row.pack()  # Pack the row below the previous ones

    # Update the scrollable region
    image_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Function for the "More" button
def load_more_images():
    global current_page, images
    query = entry.get() or 'flowers'  # Get the search query from the entry field, default to 'flowers'
    current_page += 1  # Move to the next page
    new_images = fetch_images(query, current_page)  # Fetch next set of images
    if new_images:
        images = new_images  # Replace images with the next set of images (no duplication)
        update_images()  # Update the display with new images

# Function to fetch and display the first set of images
def fetch_and_display_images():
    global images, current_page
    # Clear previous images before starting new search
    for widget in image_frame.winfo_children():
        widget.destroy()  # Destroy all previous images

    current_page = 1  # Reset to first page when new search is started
    query = entry.get() or 'flowers'  # Get the search query from the entry field, default to 'flowers'
    images = fetch_images(query, current_page)  # Fetch first set of images
    if images:
        update_images()  # Display images

# Create a text entry field for the Pixabay API search term
entry_label = tk.Label(root, text="Enter search term:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button to load the first set of images
load_button = tk.Button(root, text="Load Images", command=fetch_and_display_images)
load_button.pack(pady=10)

# Create a button to load more images
more_button = tk.Button(root, text="More", command=load_more_images)
more_button.pack(pady=10)

# Create a frame for displaying the larger image
def show_large_image(event, img):
    # Create a new window to show the larger image
    large_image_window = tk.Toplevel(root)
    large_image_window.title("Large Image View")

    # Resize the image to make it larger
    img_large = img.resize((500, 500), Image.ANTIALIAS)
    img_tk_large = ImageTk.PhotoImage(img_large)

    label = tk.Label(large_image_window, image=img_tk_large)
    label.image = img_tk_large
    label.pack(padx=20, pady=20)

    # Add a button to go back to the main window
    back_button = tk.Button(large_image_window, text="Go Back", command=large_image_window.destroy)
    back_button.pack(pady=10)

# Run the application
root.mainloop()
