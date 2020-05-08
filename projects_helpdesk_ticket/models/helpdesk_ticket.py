# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectHelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
    )

    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
    )