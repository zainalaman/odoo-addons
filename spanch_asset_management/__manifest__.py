{
    'name': 'SPANCH Asset Management',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Manage company assets, maintenance, and depreciation',
    'description': """
        Comprehensive asset management system for tracking company assets,
        maintenance schedules, depreciation calculations, and asset lifecycle.
    """,
    'author': 'Your Company',
    'website': 'https://www.spanch.my',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_views.xml',
        'views/maintenance_views.xml',
        'views/depreciation_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}