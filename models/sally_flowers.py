from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_flower = fields.Boolean("Is Flower")
    watering_frequency = fields.Integer(string="Watering Frequency (days)")
    watering_amount = fields.Float(string="Watering Amount (ml)")
    scientific_name = fields.Char(string="Scientific Name")
    season_start = fields.Date(string="Season Start")
    season_end = fields.Date(string="Season End")

    @api.model
    def _load_pos_data_domain(self, data):
        return [("is_flower", "=", True)]
    
    @api.model
    def _load_pos_data_fields(self, config_id):
        fs = super()._load_pos_data_fields(config_id)
        fs += ['is_flower','watering_frequency', 'watering_amount', 'scientific_name', 'season_start','season_end']
        return fs


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_flower = fields.Boolean("Is Flower")
    watering_frequency = fields.Integer(string="Watering Frequency (days)")
    watering_amount = fields.Float(string="Watering Amount (ml)")
    scientific_name = fields.Char(string="Scientific Name")
    season_start = fields.Date(string="Season Start")
    season_end = fields.Date(string="Season End")

    @api.model
    def _load_pos_data_domain(self, data):
        return [("is_flower", "=", True)]

    @api.model
    def _load_pos_data_fields(self, config_id):
        fs = super()._load_pos_data_fields(config_id)
        fs += ['is_flower', 'watering_frequency', 'watering_amount', 'scientific_name', 'season_start','season_end']

        return fs
    
    



