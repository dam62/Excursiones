## Gestion de Excursiones Escolares

Este modulo permite administrar excursiones escolares en Odoo, incluyendo destinos, profesores, alumnos participantes y reportes PDF.

## Funcionalidades principales

- Crear y gestionar excursiones.

- Asignar destinos y profesores responsables.

- Añadir alumnos participantes.

- Validación automática de DNI/NIE para profesores.

- Generar informe PDF con detalles de la excursión.

- Menú organizado con acceso a Excursiones, Destinos y Profesores.

## Modelos incluidos

1. Excursiones (excursiones.excursion)

- Nombre, fecha, lugar de encuentro, descripción.

- Destinos (One2many)

- Profesores (One2many)

- Alumnos (Many2many)

2. Destinos (excursiones.destino)

- Nombre del destino

- Tiempo de visita

- Excursión asociada

3. Profesores (excursiones.profesor)

- DNI validado

- Nombre

- Curso

- Telefono

- Excursion asociada

## Vistas

- Vistas tipo lista y formulario para cada modelo.

- En el formulario de excursión se muestran pestañas de Destinos y Profesores.

- Boton para generar el reporte PDF desde la excursión.

## Reporte PDF

- Nombre de la excursión

- Fecha

- Lugar de encuentro

- Descripción

- Boton "Información de la Excursion".

## Menú

- Excursiones

- Excursiones

- Destinos

- Profesores
