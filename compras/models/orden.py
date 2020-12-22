from odoo import models, fields, api

class orden(models.Model):
    _name = 'compras.orden'

    number= fields.Char(string ="N° Orden de compra")
    date = fields.Date("Fecha")
    
    detalle_Orden_ids = fields.One2many(
            'compras.detalle_orden', 'orden_id', string ="Detalle Orden"
    )

    nombreproveedor = fields.Many2one ('compras.proveedores', string = "Razón Social")


class Detalle_orden (models.Model):
    _name = 'compras.detalle_orden'
    
    nombreproducto = fields.Many2one ('compras.productos', string = "Productos")
    cantidad = fields.Integer(default =1, string = "Cantidad")
    precio = fields.Integer()
    total = fields.Integer(string ="Total", compute = "_total_orden")
    orden_id =fields.Many2one( 'compras.orden',string = "Orden")

    @api.one
    def _total_orden(self):
        self.total = (self.cantidad * self.precio)
   


