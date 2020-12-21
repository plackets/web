from odoo import models, fields, api

class compras(models.Model):
    _name = 'compras.proveedores'

    name = fields.Char(string ="Razón Social")
    ubication= fields.Char(string ="Ubicación")
    description = fields.Text(string = "Descripción")

     