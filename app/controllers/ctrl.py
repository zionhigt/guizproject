import os
from datetime import datetime

from models.line import LineModel

from services.xl import export_to_excel
from services.pdf import export_to_pdf

from logger import log

def ajouter_entree(model, form):
    def callback():
        f = {}
        for k in form:
            val = None
            if "date_" in k or "_date" in k:
                val = form.get(k).get_date().strftime("%Y-%m-%d")
            else:
                val = form.get(k).get()
            if val in [0] or val:
                f.update({
                    k: val
                })
        try:        
            model.create(f)
        except LineModel.Exception as err:
            log.error(err)
            return
        except Exception as err:
            print(err)
            return
        log.info("Enregistrement créé")
    return callback

def delete_line(model, table):
    def callback():
        selected = table.item(table.focus(), "values")
        if not selected:
            log.warn("Veuillez sélectionner une entrée à supprimer.")
            return
        if log.confirm("Voulez-vous vraiment supprimer cette entrée ?"):
            id = int(selected[0])
            model.delete(id)
    return callback

def call_finish(model, table):
    def callback():
        if not table.get_children():
            log.warn("Aucune donnée à exporter.")
            return

        export_dir = "Exports"
        os.makedirs(export_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%M")
        excel_file = os.path.join(export_dir, f"Palette_{timestamp}.xlsx")
        pdf_file = os.path.join(export_dir, f"Palette_{timestamp}.pdf")

        model_columns = model.public_header
        xl_columns = model_columns + ["Traité par ATREL", "Commentaire"]
        export_to_excel(excel_file, xl_columns, model.xl_data)

        pdf_headers = ["N° Palette", "Produit", "QTE"]
        export_to_pdf(pdf_file, pdf_headers, model.pdf_data)
        
        model.on_exported()

        log.info(f"Palette exportée :\n{excel_file}\n{pdf_file}")
        return
    return callback

def table_controller(model, table):
    def callback(model):
        table.delete(*table.get_children())
        for entry in model.entries:
            table.insert("", "end", values=[getattr(entry, col) for col in model.columns])
    model.subscribe_change(callback)

def buttons_controller(model, buttons):
    def callback(model):
        supprimer_btn = buttons.get("supprimer")
        finish_btn = buttons.get("finish")

        if model.length == 0:
            supprimer_btn.config(state="disabled")
            finish_btn.config(state="disabled")
        else:
            supprimer_btn.config(state="normal")
            finish_btn.config(state="normal")
    model.subscribe_change(callback)