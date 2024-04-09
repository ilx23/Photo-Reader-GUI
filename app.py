from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


# Function to open an image file
def open_file():
    """
        Opens an image file dialog to select an image file, then displays the selected image in the Tkinter window.

        Raises:
            Exception: If there's an error loading the image file.
        """
    # Open a file dialog to select an image file
    image_file_path = filedialog.askopenfilename(filetypes=[("Photo Files", "*.png;*.jpg;*.jpeg;*.gif;")])
    if image_file_path:
        try:
            # Open the selected image file
            img = Image.open(image_file_path)
            # Resize image if it's too large
            max_width = 600
            if img.width > max_width:
                img = img.resize((max_width, int(img.height * max_width / img.width)))

            # Convert the image to a PhotoImage object
            photo = ImageTk.PhotoImage(img)
            # Update the image label with the new image
            image_label.config(image=photo)
            image_label.image = photo
            # Change the text of the open_file_button
            open_file_button.config(text="Open Another File")
            # Adjust window size based on image dimensions
            if img.height > 500:
                app.geometry(f'{img.width + 40}x{img.height + 40}')
            else:
                app.geometry(f'{img.width + 40}x500')
        except Exception as e:
            # Show error message if there's an issue loading the image
            messagebox.showerror("Error", f"Error loading image: {e}")
    else:
        # Show warning message if no image is selected
        messagebox.showwarning("Warning", "You haven't selected any image")


# Function to close the application
def close_app():
    """Closes the Tkinter application."""
    app.destroy()


# Initialize Tkinter application
app = Tk()
app.title("Photo reader")
app.geometry("500x500")
app.config(pady=10)

# Label for displaying application title
photo_label = Label(app, text="Photo Reader", font=("Arial", 15, 'bold'))
photo_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')

# Button to open an image file
open_file_button = Button(app, text="Open File", font=("Arial", 12), borderwidth=2, relief=GROOVE, command=open_file)
open_file_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

# Button to close the application
close_button = Button(app, text="Close", font=("Arial", 12), borderwidth=2, relief=GROOVE, command=close_app)
close_button.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

# Label for displaying the image
image_label = Label(app)
image_label.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

# Configure row and column weights to center the widgets
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
app.mainloop()
