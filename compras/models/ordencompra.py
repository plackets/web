from odoo import models, fields, api

class Orden (models.Model):
    _name = 'compras.ordencompra'

    name = fields.Char(string ="Orden de compra")
    number= fields.Float (string ="N° Orden de compra")
    date= fields.Date(string ="Fecha")
    description = fields.Text(string = "Descripción")

