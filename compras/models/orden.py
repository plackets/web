

from odoo import models, fields, api

class Orden (models.Model):

    _name = 'compras.orden'

    name = fields.Char (string= "Nombre", required =True)
    apellido = fields.Char (string= "Apellido", required =True)
    number = fields.Float (string = "Número", required = True)
    date_orden = fields.Date ("Fecha")
