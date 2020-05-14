from odoo import models, fields, api

class HelpdeskTicketTeam(models.Model):
    _inherit = 'helpdesk.ticket.team'

    allow_timesheet = fields.Boolean(
        string="Allow Timesheet",
    )
    set_default_project = fields.Many2one(
        comodel_name='project.project',
        string='Default Project',
    )

#    reset_project = fields.Boolean(
#        string="Reset Project",
#    )


#   @api.onchange('allow_default_project')
#   def _onchange_reset_project(self):
#       if self.allow_default_project == False:
#           self.set_default_project = False