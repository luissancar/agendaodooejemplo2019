
from odoo import models, fields

class Comunidades(models.Model):
    _name = 'agenda.comunidades'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre de la comunidad', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res



