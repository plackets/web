from odoo import models, fields, api

class vendedor(models.Model):
    _name = 'ventas.ventas1'

    name = fields.Char(string ="Nombre", required = True)
    rut= fields.Char(string ="Rut", required = True)
    edad = fields.Integer(string = "Edad", required = True)