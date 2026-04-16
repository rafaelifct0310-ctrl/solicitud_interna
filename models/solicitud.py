from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Solicitud(models.Model):
    _name = 'solicitud.interna'
    _description = 'Solicitud Interna'
    _order = 'id desc'

    name = fields.Char(string='Número', readonly=True)
    tipo = fields.Selection([
        ('it', 'IT'),
        ('rrhh', 'RRHH'),
        ('compras', 'Compras'),
    ], string='Tipo', required=True, default='it')
    solicitante_id = fields.Many2one('res.users', string='Solicitante', default=lambda self: self.env.user)
    fecha_solicitud = fields.Datetime(string='Fecha de Solicitud', default=fields.Datetime.now, readonly=True)
    descripcion = fields.Text(string='Descripción', required=True)
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ], string='Prioridad', default='media')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('enviada', 'Enviada'),
        ('aprobada', 'Aprobada'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='borrador', readonly=True)
    respuesta = fields.Text(string='Respuesta')
    fecha_respuesta = fields.Datetime(string='Fecha de Respuesta', readonly=True)
    usuario_respuesta_id = fields.Many2one('res.users', string='Atendido por', readonly=True)
    aprobador_id = fields.Many2one('res.users', string='Aprobado por', readonly=True)
    fecha_aprobacion = fields.Datetime(string='Fecha de Aprobación', readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = self.env['ir.sequence'].next_by_code('solicitud.interna')
        return super().create(vals_list)

    def action_enviar(self):
        self.write({'estado': 'enviada'})

    def action_aprobar(self):
        self.write({
            'estado': 'aprobada',
            'aprobador_id': self.env.user.id,
            'fecha_aprobacion': fields.Datetime.now(),
        })

    def action_procesar(self):
        self.write({'estado': 'en_proceso'})

    def action_completar(self):
        self.write({
            'estado': 'completada',
            'fecha_respuesta': fields.Datetime.now(),
            'usuario_respuesta_id': self.env.user.id,
        })

    def action_cancelar(self):
        self.write({'estado': 'cancelada'})

    def action_borrador(self):
        self.write({'estado': 'borrador'})