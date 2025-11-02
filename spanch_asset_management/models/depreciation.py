from odoo import models, fields, api

class AssetDepreciation(models.Model):
    _name = 'asset.depreciation'
    _description = 'Asset Depreciation'

    name = fields.Char(string='Description', required=True)
    asset_id = fields.Many2one('asset.management', string='Asset', required=True)
    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Depreciation Amount', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], string='Status', default='draft')