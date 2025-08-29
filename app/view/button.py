
import tkinter as tk


buttons = {
        "ajouter": {
            "args": {
                "text": "Ajouter",
                "command": "ajouter_entree",
                "bg": "#eaeaea",
                "fg": "black",
                "padx": 10,
                "pady": 5,
            },
            "pack": {
                "side": "left",
                "padx": 5,
            }
        },
        "supprimer": {
            "args": {
                "text": "Supprimer",
                "command": "supprimer_entree",
                "bg": "#f44336",
                "fg": "white",
                "padx": 10,
                "pady": 5,
            },
            "pack": {
                "side": "left",
                "padx": 5,
            },
            "config": {
                "state": "disabled"
            } 
        },
        "finish": {
            "args": {
                "text": "Palette terminée",
                "command": "finish_palette",
                "bg": "#4caf50",
                "fg": "white",
                "padx": 10,
                "pady": 5,
            },
            "pack": {
                "side": "right",
                "padx": 5,
            },
            "config": {
                "state": "disabled"
            } 
        },
    }

def build_button(root, context, buttons=buttons):
    btn_frame = tk.Frame(root, pady=15, padx=15, bg="#f0f0f0")
    btn_frame.pack(fill="x")
    btns = {}
    if buttons:
        for name in buttons:
            btn = buttons[name]
            args = btn.get("args", {})
            cmd = args.get("command")
            if cmd is not None:
                cmd = context.get(cmd)
            if cmd is not None:
                args.update({
                    "command": cmd,
                })
            button = tk.Button(btn_frame, **args)
            button.pack(**btn.get("pack", {}))
            config = btn.get("config")
            if config is not None:
                button.config(**config)
            btns.update({name: button})
    return btns