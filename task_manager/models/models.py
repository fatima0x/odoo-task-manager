from odoo import models, fields

class Task(models.Model):
    _name = 'task.manager'
    _description = 'Task Manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _mail_flat_thread = False

    name = fields.Char(
        string='Task Title',
        required=True,
        tracking=True
    )
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='new', tracking=True)
    deadline = fields.Date(string='Deadline', tracking=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='low')
    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned To',
        tracking=True
    )
    customer = fields.Many2one(
        'res.partner',
        string='Related Customer',
        tracking=True
    )