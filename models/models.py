# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class pos_config(models.Model):
    _inherit = 'pos.config'


    streets = fields.Char(string='streets')
    streets2 = fields.Char(string='streets2')
    zips = fields.Char(string='zips')
    citys = fields.Char(string='citys')
    state_id = fields.Many2one('res.country.state',string="Fed. State")
    country_id = fields.Many2one('res.country',string="Country")

