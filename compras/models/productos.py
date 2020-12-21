from odoo import models, fields, api

class producto (models.Model):
    _name = 'compras.productos'

    name = fields.Char (string = "Nombre Producto", required = True)
    description = fields.Char(string ="Descripcion", required = True)
    price = fields.Float(String = "Precio")
  
    Tipo_producto_id = fields.Many2one ('compras.tipoproductos', string = "Tipo producto")
    
class Tipoproducto (models.Model):
    _name = 'compras.tipoproductos'
    name = fields.Char (string = "Nombre Producto", required = True)



