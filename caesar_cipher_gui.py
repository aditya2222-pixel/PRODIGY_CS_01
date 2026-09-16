import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def encrypt():
    try:
        shift = int(shift_entry.get())
        text = message_entry.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter a message.")
            return

        result = caesar_cipher(text, shift)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number.")

def decrypt():
    try:
        shift = int(shift_entry.get())
        text = message_entry.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter a message.")
            return

        result = caesar_cipher(text, -shift)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number.")

def clear_all():
    message_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    output_entry.delete("1.0", tk.END)

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Caesar Cipher",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

tk.Label(
    root,
    text="Enter Message",
    font=("Arial", 12, "bold")
).pack()

message_entry = tk.Text(root, height=5, width=60)
message_entry.pack(pady=10)

tk.Label(
    root,
    text="Shift Value",
    font=("Arial", 12, "bold")
).pack()

shift_entry = tk.Entry(root, width=15, font=("Arial", 12))
shift_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    command=encrypt
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    command=decrypt
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_all
).grid(row=0, column=2, padx=5)

tk.Label(
    root,
    text="Output",
    font=("Arial", 12, "bold")
).pack(pady=10)

output_entry = tk.Text(root, height=5, width=60)
output_entry.pack()

root.mainloop()