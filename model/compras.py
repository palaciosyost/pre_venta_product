from odoo import models, api, fields, _


class FechaPreVenta(models.Model):
    _inherit = "purchase.order"
    _description = "Fecha de Preventa"

    is_preventa = fields.Boolean(string="Son productos Preventa?")
    etiqueta_estado = fields.Char(string="Etiqueta Estado", store=True)

    def action_espera(self):
        if self.is_preventa and self.date_order:
            self.etiqueta_estado = "En entrega"
            for line in self.order_line:
                product = line.product_id
                product_template = line.product_id.product_tmpl_id
                if product_template:
                    product_template.fecha_preventa = self.date_planned or ""
                    product.fecha_preventa = self.date_planned or ""
        else:
            raise UserError(_("Debe contar con la fecha de entrega de los productos"))
