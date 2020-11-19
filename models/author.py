from odoo import models, api, fields
from datetime import datetime


class Author(models.Model):
    _name = 'library_management.author'
    _description = 'Tác giả'
    _oder = 'code, name, gender desc'
    _sql_constraints = [('code', 'unique(code)', 'Mã tác giả là duy nhất')]

    code = fields.Char(string='Mã')
    name = fields.Char(string='Tên')
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], default='male', string='Giới Tính')
    description = fields.Text(string='Mô tả')
    num_book = fields.Integer(string='So sach', default=0)

    def name_get(self):
        res = []
        for author in self:
            res.append((author.ids, author.code, author.name))
        return res
