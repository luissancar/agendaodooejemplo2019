from odoo import models, fields, api

class Contactos(models.Model):
    _name = 'agenda.contactos'
    dni = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    provincia = fields.Many2one('agenda.provincias', 'Provincia')



    @api.one
    def limpiar(self):
        self.nombre = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('dni', '=', '0')])
        done_recs.write({'dni': '1'})
        return True

