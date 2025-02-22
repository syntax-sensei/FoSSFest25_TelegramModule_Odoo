# telegram_notification/__manifest__.py
{
    'name': 'Telegram Notification',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for sending notifications via Telegram',
    'description': 'This module allows you to send notifications via Telegram.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base', 'sale'],
    'data': [
        'security/telegram_notification_security.xml',  # Add this line
        'security/ir.model.access.csv',
        'views/telegram_notification_views.xml',
    ],
    'installable': True,
    'application': True,
}