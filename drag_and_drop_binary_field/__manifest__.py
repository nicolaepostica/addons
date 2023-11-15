# -*- coding: utf-8 -*-
# Copyright 2023 Nicolae Postica <nicolae.postica2@gmail.com>
{
    'name': "Drag And Drop Binary Field Widget",
    'version': '17.0.1.0',
    "summary": """  
        The Drag and Drop Binary Field Widget for Odoo is a custom widget that enhances the user experience when 
        dealing with binary fields. 
    """,
    "description": """
        The Drag and Drop Binary Field Widget for Odoo is a custom widget that enhances the user experience when 
        dealing with binary fields. It enables users to easily upload files by dragging and dropping them onto the 
        binary field in Odoo forms. This documentation provides a step-by-step guide for installing, configuring, 
        and using the widget. It also includes troubleshooting tips and instructions for contributing to the widget's 
        development. By following this documentation, users and developers can effectively utilize the Drag and Drop 
        Binary Field Widget in their Odoo projects.
        """,
    'license': 'OPL-1',
    'price': 0,
    'currency': 'EUR',
    'author': "Nicolae Postica",
    'support': 'nicolae.postica2@gmail.com',
    'website': "https://github.com/nicolaepostica",
    'images': [
        'static/description/main.png',
    ],
    'category': 'Tools',
    'depends': ['base_setup'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'drag_and_drop_binary_field/static/src/js/field_binary.js',
            'drag_and_drop_binary_field/static/src/js/field_image.js',
        ],
    },
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
