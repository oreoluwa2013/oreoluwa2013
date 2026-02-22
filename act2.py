import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
    
    result_label.config(text=password)

# Create main window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x250")

# Title Label
title_label = tk.Label(window, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Length Label
length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack()

# Length Entry
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the application
window.mainloop()
