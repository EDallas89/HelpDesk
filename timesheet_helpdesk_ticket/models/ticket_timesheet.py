from odoo import models, fields, api

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    partner_phone = fields.Char(
        string='Contact Phone',
        related='partner_id.mobile',
        store=True,
        readonly=False,
    )
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analityc Account'
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
    )

    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
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

    @api.onchange('project_id')
    def _onchange_project(self):
        self.task_id = False
    
    @api.constrains('analytic_account_id')
    def _constrains_account(self):
        for record in self:
            record.timesheet_ids.update({'account_id': record.analytic_account_id.id})