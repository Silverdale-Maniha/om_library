{
    'name': 'OM Library',
    'version': '1.0',
    'summary': 'Library Management System',
    'description': 'Manage books, members, and rentals for a library.',
    'author': 'Maniha',
    'category': 'Services',
    'sequence': -101,
    'depends': ['base', 'mail'],
    'data': [
    'security/ir.model.access.csv',
    "data/library_demo.xml",
    "data/library_member_demo.xml",
    'views/books_view.xml',
    'views/authors_view.xml',
    'views/members_view.xml',
    'views/menu.xml',
    ],

    'installable': True,
    'application': True,
    'License': 'LGPL-3',
}
