from odoo import models, api, fields, _ 



class FechaPreventaProduct(models.Model):
    _inherit = "product.template"

    fecha_preventa = fields.Date(string='Fecha de Preventa')


    def limpiar_fecha_preventa (self):
        for product in self:
            fecha_hoy = fields.Date.today()
            productos = self.env["product.template"].search([("fecha_preventa", "=", fecha_hoy)])
            for producto in productos:
                producto.fecha_preventa = False