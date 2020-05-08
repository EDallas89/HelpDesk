# -*- coding: utf-8 -*-
from odoo import http

# class AnalyticAccountHelpdeskTicket(http.Controller):
#     @http.route('/analytic_account_helpdesk_ticket/analytic_account_helpdesk_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/analytic_account_helpdesk_ticket/analytic_account_helpdesk_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('analytic_account_helpdesk_ticket.listing', {
#             'root': '/analytic_account_helpdesk_ticket/analytic_account_helpdesk_ticket',
#             'objects': http.request.env['analytic_account_helpdesk_ticket.analytic_account_helpdesk_ticket'].search([]),
#         })

#     @http.route('/analytic_account_helpdesk_ticket/analytic_account_helpdesk_ticket/objects/<model("analytic_account_helpdesk_ticket.analytic_account_helpdesk_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('analytic_account_helpdesk_ticket.object', {
#             'object': obj
#         })