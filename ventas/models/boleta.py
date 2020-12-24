from odoo import models, fields, api

class boleta(models.Model):
    _name = 'ventas.boleta'

    number= fields.Char(string ="N° de boleta")
    date = fields.Date("Fecha")
    
    detalle_boleta_ids = fields.One2many(
            'ventas.detalle_boleta', 'boleta_id', string ="Detalle Boleta"
    )

    nombreproveedor = fields.Many2one ('ventas.ventas1', string = "Vendedor")


class Detalle_boleta (models.Model):
    _name = 'ventas.detalle_boleta'
    nombreproducto = fields.Many2one ('compras.productos', string = "Productos")

    cantidad = fields.Integer(default =1, string = "Cantidad")
    precio = fields.Integer()
    total = fields.Integer(string ="Total", compute = "_total_boleta")
    boleta_id =fields.Many2one( 'ventas.boleta',string = "Boleta")

    @api.one
    def _total_boleta(self):
        self.total = (self.cantidad * self.precio)
   