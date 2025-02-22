# Foss FEST 2025: International Hackathon - BSBI

# Telegram Notification Module :

This project introduces a custom Odoo module that integrates Telegram notifications into the Odoo platform. Specifically, when a sales order is created in Odoo, a notification is automatically posted to the company's warehousing Telegram channel .

This feature can be scaled to notify other departments (e.g., sales teams, logistics teams, finance teams) about relevant events. Additionally, the same functionality can be extended to other Odoo modules such as purchase orders , invoices , inventory updates , and more.

## Features

- Send Telegram notifications when a sales order is confirmed.
- Configure Telegram bot and chat IDs in Odoo.
- Easily extendable to other modules and departments.
- Supports multiple channels, groups, or individual users based on business needs.
- Detailed and professional notification messages.

## Prerequisites

- Odoo 14.0 or later
- PostgreSQL 10 or later
- Python 3.6 or later

## Installation
[Video Guide](https://www.youtube.com/watch?v=wWnZu7-63jU&list=PLX6eXpRg2kb3Zqta0tZOF_p0d_DokohhP)

## Custom Configuration

### Steps to Configure the Bot in Odoo

#### Install the Module:
1. Go to **Apps** > **Update Apps List** in Odoo.
2. Search for **Telegram Notification** and install the module.

#### Create a Telegram Bot:
1. Use **BotFather** to create a bot.
2. Retrieve the **Bot Token** from BotFather.

#### Create a Telegram Channel:
1. Create a channel (e.g., *"Warehousing Notifications"*).
2. Add the bot as an **administrator** and grant it permission to post messages.

#### Get the Channel Chat ID:
1. Post any message in the channel.
2. Use the **getUpdates API** to retrieve the Chat ID:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
3. Look for the `chat.id` value (e.g., `-100123456XXX`).

#### Configure the Bot in Odoo:
1. Search for **Telegram Notifications** in Odoo.
2. Add a new record with:
   - **Bot Name**: A descriptive name (e.g., *"Warehousing Bot"*).
   - **Bot Token**: The token obtained from BotFather.
   - **Chat IDs**: The **Channel Chat ID** (e.g., `-100123456789`).

#### Test the Configuration:
1. Confirm a **sales order** in Odoo.
2. Check the **Telegram channel/user chat** for the notification.

## Telegram Bot Link

[https://t.me/odooping_bot](https://t.me/odooping_bot)

## Telegram Test Channel Link

[https://t.me/+LVWAnb_xzVo3MmNl](https://t.me/+LVWAnb_xzVo3MmNl)

## License

This module is licensed under the  GNU LGPL Version 2.1 License. See the [LICENSE](https://github.com/open-eid/libdigidoc/blob/master/LICENSE.LGPL) file for more details.

## Author

- Aditya Bindu Sebastian - [GitHub](https://github.com/syntax-sensei) [LinkedIn](https://www.linkedin.com/in/aditya-sebastian/)
- Anmol Garg - [GitHub](https://github.com/anmollgarg) [LinkedIn](https://www.linkedin.com/in/garg-anmol/)
- Kartikey Sharma - [GitHub](https://github.com/Kartikeyy-Sharma) [LinkedIn](https://www.linkedin.com/in/kartikey-sharma-444a62257/)
