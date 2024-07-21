import tkinter as tk
from tkinter import messagebox

def login():
    if entry_username.get() == "admin" and entry_password.get() == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

root = tk.Tk()
root.title("Login")
root.configure(bg="aqua")

tk.Label(root, text="Username", bg="coral").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password", bg="coral").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
