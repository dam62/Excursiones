# -*- coding: utf-8 -*-
{
    'name': "excursiones",
    'summary': "Gestión de excursiones escolares",
    'description': """
Módulo para la planificación de excursiones escolares:
- Gestión de excursiones, destinos y profesores responsables.
- Validación de fechas.
- Generación de ficha PDF de cada excursión.
    """,

    'author': "Vicente",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '1.0',

    # Dependencias del módulo
    'depends': ['base'],

    # Archivos de datos cargados por el módulo
    'data': [
    'security/ir.model.access.csv',    
    'reports/excursiones_report.xml',    
    'views/views.xml',                   
    ],


    'application': True,
    'installable': True,
    'auto_install': False,

    # Archivos demo (opcional)
    'demo': [],
}
