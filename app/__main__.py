from models.line import LineModel

from view.interface import ui_factory
from view.product_form import build_form, options as form_options
from view.button import build_button, buttons
from view.table import build_table

from controllers.ctrl import (
    ajouter_entree,
    delete_line,
    call_finish,
    table_controller,
    buttons_controller,
)

from services.store import CsvStore

model = LineModel()

def hook_handler(hooks):
    def callback():
        for h in hooks:
            h()
    return callback

def ui():
    root = ui_factory()
    form = build_form(root, form_options)
    delete_hooks = []
    finish_hooks = []
    btns = build_button(root, {
            "ajouter_entree" : hook_handler([ajouter_entree(model, form)]),
            "supprimer_entree" : hook_handler(delete_hooks),
            "finish_palette" : hook_handler(finish_hooks),
        },
        buttons,
    )
    table = build_table(model, root)
    delete_hooks.append(delete_line(model, table))
    finish_hooks.append(call_finish(model, table))
    table_controller(model, table)
    buttons_controller(model, btns)
    return root

def flush(store):
    def callback(model):
        store.flush(model.data)
    return callback


if __name__ == "__main__":
    root = ui()
    headers = model.public_header
    store = CsvStore("./app/data/memory.csv", headers)
    store_data = store.read()
    for i, record in enumerate(store_data):
        model.create(model.hydrate(record), disabled_change=(i < len(store_data) - 1))
    model.subscribe_change(flush(store))
    root.mainloop()
