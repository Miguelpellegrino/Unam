# -*- coding: utf-8 -*-
{
    'name': "Unam addons",

    'summary': "Gestion de inscripciones",

    'description': """
        gestionar las inscripciones de alumnos en un sistema educativo
    """,

    'author': "Miguel Pellegrino ",
    'website': "https://www.linkedin.com/in/miguel-pellegrino-8a0a04198/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','contacts','product'],

    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/product_template.xml",
        "views/unam_registrations.xml",
        "views/res_partner.xml",
        "views/unam_subjects.xml",
        "views/menu.xml"
    ],
}

