from odoo import models, fields, api


class FlowerAddOns(models.Model):
    _name = "flower.addon"

    name = fields.Char(string="Add Ons Name")
    price = fields.Float(string="Add ons Price")


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_flower_addon(self):
        return {
            "search_params": {
                "domain": [],
                "fields": ["id", "name", "price"],
            }
        }

    def _get_pos_ui_flower_addon(self, params):
        return self.env["flower.addon"].search_read(**params["search_params"])
    
    def _loader_params_product_product(self):
        res = super()._loader_params_product_product()
        res["search_params"]["fields"] += ["is_flower", "addon_ids"]
        return res


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
    
class ProductOrderLine(models.Model):
    _inherit = "pos.order.line"

    addon_ids = fields.One2many("flower.addon", "id", string="Available Add-ons")


    @api.model
    def _load_pos_data_fields(self, config_id):
        fs = super()._load_pos_data_fields(config_id)
        fs += ['addon_ids']

        return fs




