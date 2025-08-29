import tkinter as tk
from tkinter import ttk

def build_table(model, root):
    columns = ["Id"] + model.public_header
    table_frame = tk.Frame(root, bg="#f0f0f0")
    table_frame.pack(fill="both", expand=True, padx=15, pady=(0,15))
    table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, minwidth=80, width=130, anchor="center")
    table.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    statut_label = tk.Label(root, text="", fg="green", bg="#f0f0f0", font=('Arial', 10))
    statut_label.pack()

    return table