# -*- coding: utf-8 -*-
{
    'name': "Analytics Accounts for Helpdesk's Tickets",
    'summary': """
        Añade las Cuentas Analíticas a los Tickets del Helpdesk""",
    'author': "Inma Sánchez",
    'website': "https://github.com/EDallas89",
    'category': 'Account',
    'version': '12.0',
    'depends': ['helpdesk_mgmt','account'],
    'data': [
        #'security/ir.model.access.csv',
        'views/analytic_account_helpdesk_ticket.xml',
    ],
    'installable': True,
    'application': True,
}