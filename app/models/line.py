class Entity:
    def __init__(self, vals):
        for k in vals:
            v = vals[k]
            setattr(self, k, v)
    
    def __hash__(self):
        return self.id

class ModelException(Exception):
    pass

class LineModel:
    Exception = ModelException
    def __init__(self):
        self.change_hooks = []
        self.increment = 1
        self.required_field = [
            "no_palette",
            "produit",
            "qte",
        ]
        self.translated_columns = [
            ("id", "Id"),
            ("date_reception", "Date réception"),
            ("no_palette", "N° palette"),
            ("produit", "Produit"),
            ("qte", "QTE"),
            ("sn_fictif", "SN FICTIF"),
            ("sn_reel", "SN REEL"),
            ("date_expedition", "Date expédition"),
        ]
        self.entries = set([])
    
    @property
    def columns(self):
        return list(map(lambda x: x[0], self.translated_columns))
    
    @property
    def length(self):
        return len(self.entries)
    
    @property
    def xl_data(self):
        data = []
        for entry in self.entries:
            data.append([getattr(entry, k) for k in self.columns if k != "id"] + ["", ""])
        return data
    
    @property
    def pdf_data(self):
        data = []
        for entry in self.entries:
            data.append([
                getattr(entry, "no_palette"),
                getattr(entry, "produit"),
                getattr(entry, "qte"),
            ])
        return data
    
    @property
    def data(self):
        res = []
        for entry in self.entries:
            record = {}
            for field in self.columns:
                if field == "id":
                    continue
                record[field] = getattr(entry, field)
            res.append(record)
        return res

    @property
    def public_header(self):
        return [dict(self.translated_columns)[field] for field in self.columns if field != "id"]

    def subscribe_change(self, fn):
        self.change_hooks.append(fn)

    def on_change(self):
        for fn in self.change_hooks:
            fn(self)
    
    def on_exported(self):
        self.entries = set([])
        self.increment = 1
        self.on_change()

    def get_next_id(self):
        i = self.increment
        self.increment += 1
        return i
    
    def create(self, vals, disabled_change=False):
        record = {i: None for i in self.columns}
        for field in self.columns:
            val = vals.get(field)
            if field in self.required_field and val is None:
                raise LineModel.Exception(f"Champ manquant : ({dict(self.translated_columns)[field]})")
            record.update({
                field: val
            })

        record.update({
            "id": self.get_next_id()
        })
        entry = Entity(record)
        self.entries.add(entry)
        if not disabled_change:
            self.on_change()
    
    def delete(self, id):
        target = None
        for entry in self.entries:
            if entry.id == id:
                target = entry
                break
        if target is not None:
            self.entries.remove(target)
            self.on_change()
    
    def hydrate(self, record):
        res = {}
        for field, trans in self.translated_columns:
            target = record.get(trans)
            if target is not None:
                res[field] = target
        return res