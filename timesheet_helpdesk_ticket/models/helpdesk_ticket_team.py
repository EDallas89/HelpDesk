from odoo import models, fields, api

class HelpdeskTicketTeam(models.Model):
    _inherit = 'helpdesk.ticket.team'

    allow_timesheet = fields.Boolean(
        string="Allow Timesheet",
    )
