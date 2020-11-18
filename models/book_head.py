from odoo import models, fields, api


class BookHead(models.Model):
    _name = 'library_management.book_head'
    _order = 'book_head_code, book_head_name desc'

    book_head_code = fields.Char(string='Mã')
    book_head_name = fields.Char(string='Tên', required=True)
    book_head_description = fields.Text(string='Mô tả')
    category_display = fields.Many2many('library_management.category',
                                     index=True,
                                     string='Tên dau Sách')
