from odoo import models, fields, api

class UnamRegistrations(models.Model):
    _name = 'unam.registrations'
    
    student_id = fields.Many2one('res.partner', string="Estudiante", required=True, domain=[('is_teacher', '=', False)])
    course_id = fields.Many2one('product.template', string="Curso", required=True, domain=[('detailed_type','=','consu'),('course_ok','=',True)])
    enrollment_date = fields.Date(string="Fecha de inscripcion", default=fields.Date.today, required=True)
    
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
    ], string='Status', default='pending', required=True)

    note = fields.Text(string="Nota")
    name = fields.Char(string='Nombre', store=True, default="New", readonly=True)

    def action_confirmed(self):
        self.write({
            'state':'confirmed'
        })

    def action_cancelled(self):
        self.write({
            'state':'cancelled'
        })

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('unam.registrations') or ('New')
        return super().create(vals_list)
