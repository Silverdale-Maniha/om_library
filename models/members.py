from odoo import models, fields

class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"

    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    membership_start = fields.Date(string="Membership Start")
    membership_end = fields.Date(string="Membership End")
    membership_type = fields.Selection([
        ('basic', 'Basic'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum')
    ], string="Membership Type", default='basic')
