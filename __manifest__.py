{
    'name': 'Custom Invoice Header',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Customize invoice header to show invoice number from page 2 onwards',
    'description': """
        This module modifies the invoice report to show the invoice number
        in the header from page 2 onwards, opposite to the logo and company information.
    """,
    'author': 'Lasse Larsson, Kubang AB',
    'website': 'https://www.kubang.eu',
    'depends': ['web', 'account'],
    'data': [
        'views/report_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
