# -*- coding: utf-8 -*-
from odoo import http

# class ProjectHelpdeskTicket(http.Controller):
#     @http.route('/project_helpdesk_ticket/project_helpdesk_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_helpdesk_ticket/project_helpdesk_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_helpdesk_ticket.listing', {
#             'root': '/project_helpdesk_ticket/project_helpdesk_ticket',
#             'objects': http.request.env['project_helpdesk_ticket.project_helpdesk_ticket'].search([]),
#         })

#     @http.route('/project_helpdesk_ticket/project_helpdesk_ticket/objects/<model("project_helpdesk_ticket.project_helpdesk_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_helpdesk_ticket.object', {
#             'object': obj
#         })