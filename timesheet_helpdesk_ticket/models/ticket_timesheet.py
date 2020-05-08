from odoo import models, fields, api

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    partner_phone = fields.Char(
        string='Contact Phone',
        related='partner_id.mobile',
        store=True,
        readonly=False,
    )
    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )

    total_hours_ticket = fields.Float(
        compute='impute_hours',
    )

    @api.depends('timesheet_ids.unit_amount')
    def impute_hours(self):
        for record in self:
            record.total_hours_ticket = sum(record.timesheet_ids.mapped('unit_amount'))
