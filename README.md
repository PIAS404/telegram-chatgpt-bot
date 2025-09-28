Telegram ChatGPT Bot
A Telegram bot integrated with OpenAI's ChatGPT API to respond to user messages.
Prerequisites

Python 3.8+
Telegram Bot API token (get from @BotFather)
OpenAI API key (get from platform.openai.com)
Git installed
A GitHub account

Setup Instructions

Clone the repository:
git clone https://github.com/YOUR_USERNAME/telegram-chatgpt-bot.git
cd telegram-chatgpt-bot


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Set up environment variables:

Create a .env file in the root directory.
Add your API keys:TELEGRAM_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here




Run the bot:
python bot.py


Test the bot:

Open Telegram, search for your bot (e.g., @MyChatGPTBot).
Send /start or any message to interact.



Deployment (Optional)
To run the bot 24/7, deploy it to a server like Heroku, Render, or AWS:

For Heroku, create a Procfile with: worker: python bot.py.
Set environment variables in the hosting platform's dashboard.
Follow the platform's deployment guide.

Notes

Keep your .env file secure and never commit it to Git.
Check OpenAI's rate limits and pricing to avoid unexpected costs.
For advanced features, add conversation history by storing messages in the openai.ChatCompletion.create call.

License
MIT
