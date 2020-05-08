# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectHelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analityc Account',
    )