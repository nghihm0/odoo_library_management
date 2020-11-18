# -*- coding: utf-8 -*-
{
    'name': "library_management",

    'summary': """ Library management """,

    'description': """
        This app for library management for:
            - Category
            - Book
            - Author
            - Publisher
    """,

    'author': "Author",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/category.xml',
        'views/book_head.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installation': True,
    'application': True,
}
