# Telegram Media Bot

This bot is designed to automatically scan a specified directory for media files (such as photos, videos, and documents) and send each file to a designated Telegram channel at user-defined intervals. It also supports custom message captions and interactive inline buttons.

## Features

- Scans a specified directory for media files.
- Sends media files to a designated Telegram channel.
- Customizable send intervals for media files.
- Supports custom captions and inline interactive buttons.
- Easy to set up and use.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6+
- A Telegram Bot Token
- A Telegram Channel ID

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-media-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd telegram-media-bot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root and add your Telegram Bot Token and Channel ID:
   ```plaintext
   BOT_TOKEN=your_bot_token
   CHAT_ID=your_channel_id
   ```
2. Add any additional configuration parameters as needed.

## Usage

To start the bot, run:
```bash
python main.py
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.





Project Link: [https://github.com/yourusername/telegram-media-bot](https://github.com/yourusername/telegram-media-bot)
