from odoo import models, api, fields, _ 



class FechaPreventaProduct(models.Model):
    _inherit = "product.template"

    fecha_preventa = fields.Date(string='Fecha de Preventa')


    @api.model
    def limpiar_fecha_preventa(self):
        fecha_hoy = fields.Date.today()
        self.sudo().search([("fecha_preventa", "=", fecha_hoy)]).write({"fecha_preventa": False})