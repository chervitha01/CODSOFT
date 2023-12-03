import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#3498db", fg="white")
generate_button.grid(row=1, columnspan=2, padx=5, pady=5)

password_entry = tk.Entry(frame, show="", bg="#ffffff")
password_entry.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
