# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'library_management.category'
    _description = 'Library category'
    _oder = 'category_id ,name, num_book desc'
    _sql_constraints = {
        ('code', 'unique(code)', ''),
        ('name', 'unique(name)', 'Please enter unique name of category')
    }

    category_code = fields.Char(string='Mã')
    category_name = fields.Char(string='Tên', required=True)
    category_description = fields.Text(string='Mô Tả')
    num_book = fields.Integer(string='Tổng số sách', default=0)

    def name_get(self):
        names = []
        for category in self:
            names.append((category.id, category.category_name))
        return names




