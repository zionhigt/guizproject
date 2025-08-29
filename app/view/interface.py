import tkinter as tk
from tkinter import messagebox, ttk

available_style_key = set([
    "Treeview.Heading",
    "Treeview",
])

def set_style(root, options):
    style = ttk.Style(root)
    style.theme_use('clam')
    for key in options:
        if key in available_style_key:
            style.configure(key, **options.get(key, ""))
    style.map("Treeview", **options.get("main_frame", {}))

def ui_factory():
    root = tk.Tk()
    root.title("Gestion de Données Simple")
    root.geometry("1440x720")
    root.configure(bg="#f0f0f0")

    # option; peut être charger en config
    options = {
        "Treeview.Heading": {
            "font": ('Arial', 11, 'bold'),
            "background": "#444",
            "foreground": "white",
        },
        "Treeview": {
            "font": ('Arial', 10),
            "rowheight": 25
        },
        "main_frame": {
            "background": [('selected', '#6a9fb5')],
            "foreground": [('selected', 'white')]
        }
    }
    set_style(root, options)

    return root