import tkinter as tk

from tkcalendar import DateEntry

def build_form(root, options):
    main_frame_options = options.get("main_frame")
    if main_frame_options is None:
        main_frame_options = {
            "padx": 15,
            "pady": 15,
            "bg": "#f0f0f0"
        }
    # FORM
    form_frame = tk.Frame(root, **main_frame_options)
    main_frame_config_fill = options.get("main_frame_config_fill", "x")
    form_frame.pack(fill=main_frame_config_fill)
    form = {}
    for inp in options.get("inputs", []):
        tk.Label(form_frame, **inp.get("label")).grid(**inp.get("label_grid"))
        entry = inp.get("constructor")
        if entry:
            entry = entry(form_frame, **inp.get("args", {}))
            entry.grid(**inp.get("entry_grid"))
            form_key = inp.get("name")
            if form_key:
                form.update({
                    form_key: entry,
                })
    for i in range(4):
        form_frame.columnconfigure(i, weight=3**(i % 2))
    
    return form

"date_reception",
"no_palette",
"produit",
"qte",
"sn_fictif",
"sn_reel",
"date_expedition"
options = {
    "inputs": [
        {
            "name": "date_reception",
            "label": {
                "text": "Date réception",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 0,
                "column": 0,
                "sticky": "w"
            },
            "constructor": DateEntry,
            "args": {"width": 12},
            "entry_grid": {
                "row": 0,
                "column": 1,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "no_palette",
            "label": {
                "text": "N° palette",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 0,
                "column": 2,
                "sticky": "w"
            },
            "constructor": tk.Entry,
            "args": {},
            "entry_grid": {
                "row": 0,
                "column": 3,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "produit",
            "label": {
                "text": "Produit",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 1,
                "column": 0,
                "sticky": "w"
            },
            "constructor": tk.Entry,
            "args": {},
            "entry_grid": {
                "row": 1,
                "column": 1,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "qte",
            "label": {
                "text": "QTE",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 1,
                "column": 2,
                "sticky": "w"
            },
            "constructor": tk.Entry,
            "args": {},
            "entry_grid": {
                "row": 1,
                "column": 3,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "sn_fictif",
            "label": {
                "text": "SN FICTIF",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 2,
                "column": 0,
                "sticky": "w"
            },
            "constructor": tk.Entry,
            "args": {},
            "entry_grid": {
                "row": 2,
                "column": 1,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "sn_reel",
            "label": {
                "text": "SN REEL",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 2,
                "column": 2,
                "sticky": "w"
            },
            "constructor": tk.Entry,
            "args": {},
            "entry_grid": {
                "row": 2,
                "column": 3,
                "sticky": "ew",
                "padx": 5,
            }
        },
        {
            "name": "date_expedition",
            "label": {
                "text": "Date expédition",
                "bg": "#f0f0f0",
            },
            "label_grid": {
                "row": 3,
                "column": 0,
                "sticky": "w"
            },
            "constructor": DateEntry,
            "args": {"width": 12},
            "entry_grid": {
                "row": 3,
                "column": 1,
                "sticky": "ew",
                "padx": 5,
            }
        }]
}