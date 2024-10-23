from odoo import models, fields

class UnamSubject(models.Model):
    _name = 'unam.subject'
    
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripcion")
    credits = fields.Integer(string="Creditos", required=True)
