from odoo import models, fields

class CRMStage(models.Model):
    _inherit = 'crm.stage'

    custom_field = fields.Char(string="Campo Personalizado")
