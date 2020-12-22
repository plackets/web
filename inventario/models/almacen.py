# -*- coding: utf-8 -*-

from odoo import models, fields, api

class almacenamiento(models.Model):
     _name = 'inventario.almacenamiento'

     name = fields.Char(string = "Nombre", required = True)
     almacen_ids = fields.One2many(
          'inventario.almacen', #related model
          'almacenamiento_id', # field for "this" on related model
          string='Inventario')

     total_estados = fields.Integer(
          string="Total de estados", compute="_total_estados")

     @api.one
     def _total_estados(self):
          self.total_estados = len(self.almacen_ids)

class inventario(models.Model):
     _name = 'inventario.almacen'

     nombre = fields.Char()
     cantidad = fields.Integer()
     fecha = fields.Date("Fecha")
     porcentaje = fields.Text(string="% de uso")

     almacenamiento_id = fields.Many2one('inventario.almacenamiento', string = 'Almacenamiento')