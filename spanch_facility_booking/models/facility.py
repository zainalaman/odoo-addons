from odoo import models, fields

class Facility(models.Model):
    _name = 'facility'
    _description = 'Facility'

    name = fields.Char(string='Facility Name', required=True)
    code = fields.Char(string='Facility Code', required=True)
    facility_type = fields.Selection([
        ('meeting_room', 'Meeting Room'),
        ('conference_hall', 'Conference Hall'),
        ('training_room', 'Training Room'),
        ('other', 'Other')
    ], string='Facility Type', default='meeting_room')
    
    capacity = fields.Integer(string='Capacity')
    location = fields.Char(string='Location')
    description = fields.Text(string='Description')