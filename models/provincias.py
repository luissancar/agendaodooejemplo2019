from odoo import models, fields, api

class Provincias(models.Model):
    _name = 'agenda.provincias'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre', required=True)
    comunidad = fields.Many2one('agenda.comunidades', 'Comunidad')


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

