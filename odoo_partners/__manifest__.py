# -*- coding: utf-8 -*-
{
    'name': "odoo_partners",
    'summary': """
        Get official odoo partners from https://odoo.com/partners""",
    'description': """ Get official odoo partners from https://odoo.com/partners,
    update data every month""",
    'author': "Anonymous",
    'price': 300,
    'currency': 'EUR',
    'support': 'support@gmail.com',
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",
    'category': 'Automation',
    'version': '16.0.0.1',
    'external_dependencies': {
        'python': ['beautifulsoup4'],
    },
    'depends': ['base'],
    'data': [
        # Data
        'data/res_partner_category.xml',
        # Cron
        'views/ir_cron.xml'
    ],
    'demo': [],
}
