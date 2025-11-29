# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

# ----------------------------
# MODELO EXCURSION
# ----------------------------
class Excursion(models.Model):
    _name = 'excursiones.excursion'
    _description = 'Excursiones escolares'
    _rec_name = 'nombre_excursion'

    nombre_excursion = fields.Char(string="Nombre de la excursión", required=True, default="Nueva Excursión")
    fecha_excursion = fields.Datetime(string='Fecha de la excursión', required=True)
    lugar_encuentro = fields.Char(string='Lugar de encuentro', required=True)
    descripcion_excursion = fields.Char(string='Información de la excursión')

    ids_destino = fields.One2many('excursiones.destino', 'id_excursion', string='Destinos')
    ids_profesor = fields.One2many('excursiones.profesor', 'id_excursion', string='Profesores responsables')

    alumnos = fields.Many2many('excursiones_participantes.alumno', string="Alumnos")

    #autorizaciones = fields.One2many(
    #    'excursiones_participantes.autorizacion',
    #   'id_excursion',
    #    string='Autorizaciones'
    #)

    @api.depends('ids_destino')
    def _compute_autorizaciones(self):
        for excursion in self:
            autorizaciones = self.env['excursiones_participantes.autorizacion'].search([
                ('id_excursion', '=', excursion.id)
            ])
            excursion.autorizaciones = autorizaciones

# ----------------------------
# MODELO DESTINO
# ----------------------------
class Destino(models.Model):
    _name = 'excursiones.destino'
    _description = 'Destino de la excursión'
    _rec_name = 'nombre_destino'

    nombre_destino = fields.Char(string='Lugar del destino', required=True)
    tiempo_visita = fields.Integer(string='Duración de la visita (horas)', required=True)
    id_excursion = fields.Many2one('excursiones.excursion', string='Excursión', ondelete='cascade')

# ----------------------------
# MODELO PROFESOR
# ----------------------------
class Profesor(models.Model):
    _name = 'excursiones.profesor'
    _description = 'Profesor responsable de la excursión'
    _rec_name = 'nombre_profesor'

    dni_profesor = fields.Char(string='DNI', required=True)
    nombre_profesor = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    curso = fields.Selection([
        ('ESO1', '1ª ESO'),
        ('ESO2', '2ª ESO'),
        ('ESO3', '3ª ESO'),
        ('ESO4', '4ª ESO'),
        ('Bach1', '1ª Bachillerato'),
        ('Bach2', '2ª Bachillerato')
    ], string='Curso', required=True)
    id_excursion = fields.Many2one('excursiones.excursion', string='Excursión', ondelete='cascade')

    @api.constrains('dni_profesor')
    def _check_dni(self):
        from datetime import date
        for profesor in self:
            if profesor.dni_profesor and not validar_dni(profesor.dni_profesor):
                raise exceptions.ValidationError("El DNI introducido no es correcto")


# ----------------------------
# FUNCION VALIDAR DNI
# ----------------------------
def validar_dni(dni):
    dni = dni.upper().strip()
    if len(dni) != 9:
        return False
    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    cuerpo = dni[:-1]
    letra_introducida = dni[-1]
    if cuerpo[0] in 'XYZ':
        mapeo_nie = {'X': '0', 'Y': '1', 'Z': '2'}
        cuerpo = mapeo_nie[cuerpo[0]] + cuerpo[1:]
    if not cuerpo.isdigit() or len(cuerpo) != 8:
        return False
    numero = int(cuerpo)
    letra_calculada = LETRAS_DNI[numero % 23]
    return letra_introducida == letra_calculada
