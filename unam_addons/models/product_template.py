from odoo import models, fields

class CourseProduct(models.Model):
    _inherit = 'product.template' 
    
    teacher_ids = fields.Many2many('res.partner', string="Profesor", domain=[('is_teacher', '=', True)])
    subject_ids = fields.Many2many('unam.subject', string="Materias")
    start_date = fields.Date(string="Fecha de inicio", required=True)
    duration = fields.Integer(string="Duracion (Dias)", required=True)
    max_capacity = fields.Integer(string="Capacidad maxima de alumnos", required=True)  # Capacidad máxima de alumnos
    course_ok = fields.Boolean(string="Puede ser un curso")
    