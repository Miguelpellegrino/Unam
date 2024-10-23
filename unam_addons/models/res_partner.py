from odoo import models, api, fields
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ################################# Datos de Alumnos #######################################
    birthdate = fields.Date(string="Fecha de nacimiento")
    age = fields.Integer(string="Edad", compute='_compute_age', store=True)
    enrollment_ids = fields.One2many('unam.registrations', 'student_id', string="Inscripciones", readonly=True)
    
    ################################# Datos de Maestro #######################################
    is_teacher = fields.Boolean(string="Es maestro", default=False, readonly=True)
    course_ids = fields.Many2many('unam.subject',string="Materias")

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                birthdate = record.birthdate
                record.age = today.year - birthdate.year - (
                    (today.month, today.day) < (birthdate.month, birthdate.day)
                )
            else:
                record.age = 0