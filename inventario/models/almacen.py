# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inventario(models.Model):
     _name = 'inventario.almacen'

     nombre = fields.Char()
     cantidad = fields.Integer()
     porcentaje = fields.Text(string="% de uso")
