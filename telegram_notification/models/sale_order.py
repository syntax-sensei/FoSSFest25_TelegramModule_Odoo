
from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Call the original method to ensure the confirmation process works as usual
        res = super(SaleOrder, self).action_confirm()

        # Trigger a Telegram notification
        bot = self.env['telegram.notification'].search([], limit=1)
        if bot:
            message = (
                f"📢 <b>New Sales Order Confirmed</b> 📢\n"
                f"-----------------------------------------\n"
                f"• <b>Order Reference:</b> {self.name}\n"
                f"• <b>Customer:</b> {self.partner_id.name}\n"
                f"• <b>Total Amount:</b> {self.amount_total} {self.currency_id.symbol}\n"
                f"• <b>Order Date:</b> {self.date_order.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"• <b>Delivery Address:</b>\n"
                f"  {self.partner_shipping_id.contact_address or 'N/A'}\n"
                f"• <b>Payment Terms:</b> {self.payment_term_id.name or 'Immediate Payment'}\n"
                f"-----------------------------------------\n"
                f"🚚 <b>Delivery Information</b> 🚚\n"
            )
            bot.send_message(message)
        else:
            print("No Telegram bot configuration found. Please configure the bot in Odoo.")

        return res