{
    'name': 'SPANCH Facility Booking',
    'version': '19.0.1.0.0',
    'category': 'SPANCH',
    'summary': 'Manage facility bookings and reservations',
    'description': """
        Simple facility booking system for managing room reservations.
    """,
    'author': 'ZAS',
    'website': 'https://www.spanch.my',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/facility_views.xml',
        'views/booking_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}