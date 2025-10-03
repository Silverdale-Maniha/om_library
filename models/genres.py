from odoo import models, fields

class LibraryGenre(models.Model):
    _name = "library.genre"
    _description = "Book Genre"

    name = fields.Char("Genre", required=True)
    color = fields.Integer("Color")
