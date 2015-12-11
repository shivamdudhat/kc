# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Synchronization with the external timesheet application',
    'version': '1.0',
    'category': 'Project & Timesheet Management',
    'description': """
Synchronization of timesheet entries with the external timesheet application.
====================================================================

If you use the external timesheet application, this module alows you to synchronize timesheet entries between Odoo and the application.
    """,
    'author': 'Odoo SA',
    'website': 'https://www.odoo.com/page/project-management',
    'images': ['images/invoice_task_work.jpeg', 'images/my_timesheet.jpeg', 'images/working_hour.jpeg'],
    'depends': ['project_timesheet', 'hr_timesheet_sheet'],
    'data': [
        'views/templates.xml',
        'views/timesheet_views.xml',
    ],
    'qweb': [
        'static/src/xml/timesheet_app_backend_template.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
