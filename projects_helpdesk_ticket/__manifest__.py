# -*- coding: utf-8 -*-
{
    'name': "Project for Helpdesk's Tickets",
    'summary': """
        Añade Proyectos a los Tickets del Helpdesk""",
    'author': "Inma Sánchez",
    'website': "https://github.com/EDallas89",
    'category': 'Project',
    'version': '12.0',
    'depends': ['helpdesk_mgmt','project'],
    'data': [
        #'security/ir.model.access.csv',
        'views/project_helpdesk_ticket.xml',
    ],
    'installable': True,
    'application': True,
}