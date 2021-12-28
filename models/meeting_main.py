from odoo import models, fields, api
from odoo.exceptions import ValidationError


class KrHuiyi(models.Model):
    _name = 'meeting.main'
    _description = '會議'
    _order = 'start_time desc'

    name = fields.Many2one('meeting.site', string='會議地點', required=True)
    start_time = fields.Datetime('開始時間', required=True)
    end_time = fields.Datetime('結束時間')
    remark = fields.Char('備註')

    @api.constrains('end_time')
    def _check_end_time(self):
        for record in self:
            if record.start_time > record.end_time:
                raise ValidationError('結束時間不可以早於開始時間！')
