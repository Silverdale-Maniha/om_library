from odoo import models, fields, api
from datetime import date

class LibraryBookLoan(models.Model):
    _name = "library.book.loan"
    _description = "Library Book Loan"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    member_id = fields.Many2one('library.member', string="Member", required=True)
    book_id = fields.Many2one('library.book', string="Book", required=True)
    loan_date = fields.Date(string="Loan Date", default=fields.Date.context_today)
    return_date = fields.Date(string="Return Date")
    state = fields.Selection(
        [('borrowed', 'Borrowed'),
         ('returned', 'Returned'),
         ('late', 'Late')],
        string="Status",
        default="borrowed",
        tracking=True
    )

    @api.model
    def create(self, vals):
        record = super(LibraryBookLoan, self).create(vals)
        if record.book_id and record.book_id.available_copies > 0:
            record.book_id.available_copies -= 1
        return record

    def action_return(self):
        for rec in self:
            if rec.state == "borrowed":
                rec.state = "returned"
                rec.return_date = date.today()
                rec.book_id.available_copies += 1
