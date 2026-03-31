from odoo import models, fields

class Task(models.Model):
    _name = 'task.manager'
    _description = 'Task Manager'

    name = fields.Char(string='Task Title', required=True)
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='new')
    deadline = fields.Date(string='Deadline')
