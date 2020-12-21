# -*- coding: utf-8 -*-
{
    'name': "ventas",

    'summary': """
        ventas de gustoso""",

    'description': """
        modulo que gestiona las ventas del restaurant gustoso
    """,

    'author': "hectorin19",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # aquí se coloca de que modulo depende este 
    'depends': ['base'], 

    # always loaded
    'data': [
        # 'security/ir.model.access.csv', que datos voy a ocupar
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
   # 'demo': [
    #    'demo/demo.xml',
    #],
}