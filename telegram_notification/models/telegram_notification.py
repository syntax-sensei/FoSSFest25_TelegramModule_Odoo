# telegram_notification/models/telegram_notification.py
import requests
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class TelegramNotification(models.Model):
    _name = 'telegram.notification'
    _description = 'Telegram Notification Configuration'

    name = fields.Char(string='Bot Name', required=True)
    token = fields.Char(string='Bot Token', required=True)
    chat_ids = fields.Text(string='Chat IDs', help="Comma-separated list of Telegram chat IDs")

    def send_message(self, message, chat_id=None):
        """Send a message via Telegram Bot API."""
        if not chat_id:
            chat_ids = self.chat_ids.split(',')
            for chat_id in chat_ids:
                self._send_to_chat(chat_id.strip(), message)
        else:
            self._send_to_chat(chat_id, message)

    def _send_to_chat(self, chat_id, message):
        """Internal method to send a message to a specific chat."""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code != 200:
                _logger.error(f"Failed to send message: {response.text}")
                raise Exception(f"Failed to send message: {response.text}")
            _logger.info(f"Message sent successfully to chat_id: {chat_id}")
        except Exception as e:
            _logger.error(f"Error sending message: {str(e)}")