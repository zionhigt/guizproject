from tkinter import messagebox

def info(msg):
    messagebox.showinfo("Succès", msg)

def warn(msg):
    messagebox.showwarning("Attention", msg)

def error(msg):
    messagebox.showerror("Erreur", msg)

def confirm(msg):
    return messagebox.askyesno("Confirmation", msg)