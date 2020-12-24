# -*- coding: utf-8 -*-
{
    'name': "Ventas",

    'summary': """
        Proceso de ventas""",

    'description': """
        Modulo que gestiona las ventas del restaurant Gustoso
    """,

    'author': "hectorin19",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # aquí se coloca de que modulo depende este 
    'depends': ['base','compras'], 

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_vendedor.xml',
        'views/view_boleta.xml',
    ],
    'application': True,
}