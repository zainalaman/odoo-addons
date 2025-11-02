from odoo import models, fields, api

class AssetManagement(models.Model):
    _name = 'asset.management'
    _description = 'Asset Management'

    name = fields.Char(string='Asset Name', required=True)
    code = fields.Char(string='Asset Code', required=True)
    asset_category_id = fields.Many2one('asset.category', string='Category')
    purchase_date = fields.Date(string='Purchase Date')
    purchase_cost = fields.Float(string='Purchase Cost')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('retired', 'Retired')
    ], string='Status', default='draft')

class AssetCategory(models.Model):
    _name = 'asset.category'
    _description = 'Asset Category'
    
    name = fields.Char(string='Category Name', required=True)
    code = fields.Char(string='Category Code')

class AssetLocation(models.Model):
    _name = 'asset.location'
    _description = 'Asset Location'
    
    name = fields.Char(string='Location Name', required=True)
    code = fields.Char(string='Location Code')