from odoo import models, fields, api

class AssetMaintenance(models.Model):
    _name = 'asset.maintenance'
    _description = 'Asset Maintenance'

    name = fields.Char(string='Maintenance Reference', required=True)
    asset_id = fields.Many2one('asset.management', string='Asset', required=True)
    maintenance_type = fields.Selection([
        ('preventive', 'Preventive Maintenance'),
        ('corrective', 'Corrective Maintenance')
    ], string='Maintenance Type', default='preventive')
    
    scheduled_date = fields.Date(string='Scheduled Date')
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed')
    ], string='Status', default='draft')

class MaintenancePartLine(models.Model):
    _name = 'maintenance.part.line'
    _description = 'Maintenance Part Line'
    
    maintenance_id = fields.Many2one('asset.maintenance', string='Maintenance', required=True)
    product_id = fields.Many2one('product.product', string='Product')
    product_uom_qty = fields.Float(string='Quantity', default=1.0)