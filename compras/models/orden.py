from odoo import models, fields, api

class orden(models.Model):
    _name = 'compras.orden'

    name = fields.Char(string ="Razón Social")
    number= fields.Char(string ="N° Orden de compra")
    date = fields.Date("Fecha")

