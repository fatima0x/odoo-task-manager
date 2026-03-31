{
    'name': 'Task Manager',
    'version': '1.1',
    'category': 'Productivity',
    'summary': 'Simple Task Manager CRUD app',
    'description': 'A simple module to create and manage tasks with user assignment and messaging',
    'author': 'Fatima Suleman',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}