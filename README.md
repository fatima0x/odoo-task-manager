# Odoo Task Manager Module

A custom Odoo 17 module for task management built with Python 3.13.

## Features
- Full CRUD operations (Create, Read, Update, Delete)
- Priority levels (Low, Medium, High)
- Assign tasks to real Odoo users
- Link tasks to customers/contacts
- Kanban view grouped by status
- List and Form views
- Field change tracking via mail module

## Intermodular Connections
- `res.users` — task assignment (base module)
- `res.partner` — customer linking (base module)
- `mail.thread` — change tracking (mail module)

## Tech Stack
- Odoo 17
- Python 3.13
- PostgreSQL

## Installation
1. Clone this repo into your Odoo addons folder
2. Restart Odoo with `-u task_manager`
3. Install from Apps menu

## Author
Fatima Suleman
