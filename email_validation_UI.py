# email_validator_ui.py

import tkinter as tk
from tkinter import messagebox
from email_validator import is_valid_email  # Import the email validation function

# Function to validate email
def validate_email():
    email = email_entry.get()
    if is_valid_email(email):
        result_label.config(text="Valid Email", fg="green")
    else:
        result_label.config(text="Invalid Email", fg="red")

# Create the main window
root = tk.Tk()
root.title("Email Validator")
root.geometry("300x200")

# Create a label for the email entry
email_label = tk.Label(root, text="Enter your email:")
email_label.pack(pady=10)

# Create an entry field for the email
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Create a button to validate the email
validate_button = tk.Button(root, text="Validate", command=validate_email)
validate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
