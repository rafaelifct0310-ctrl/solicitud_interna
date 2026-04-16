{
    'name': 'Solicitud Interna',
    'version': '19.0.1.0.0',
    'category': 'General',
    'summary': 'Gestión de solicitudes internas (IT, RRHH, Compras)',
    'description': '''
        Permite registrar y gestionar solicitudes internas para los departamentos de:
        - IT (Soporte Técnico)
        - RRHH (Recursos Humanos)
        - Compras (Adquisiciones)
    ''',
    'author': 'Rafael Martín',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/solicitud_security.xml',
        'security/ir.model.access.csv',
        'data/solicitud_data.xml',
        'views/solicitud_views.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}