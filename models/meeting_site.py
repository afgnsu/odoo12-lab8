from odoo import fields, api, models


class KrSite(models.Model):
    _name = 'meeting.site'
    _description = '會議地點'

    name = fields.Char('地點')
    huiyi_ids = fields.One2many('meeting.main', 'name', string='會議')
