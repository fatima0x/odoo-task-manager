{
    'name': 'Task Manager',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Simple Task Manager CRUD app',
    'description': 'A simple module to create and manage tasks',
    'author': 'Fatima Suleman',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}