# URL Encoding Bot

This repository contains a Telegram bot built using the Pyrogram framework. The bot provides a simple utility to encode text into URL-friendly format, making it easier to create links or share special characters in URLs.

## Features
- Accepts user input via the `/encode` command.
- Converts the provided text into URL-encoded format.
- Replies with the encoded result, which can be used in applications like Telegram links, web forms, and more.

## Example Usage
1. Send the bot a message with thre text you want to encode:
   ```
   Hello World!
   ```

2. The bot replies with:
   ```
   Encoded URL: `Hello+World%21`
   ```

## Requirements
- Python 3.7+
- Pyrogram
- A Telegram bot token (can be obtained from BotFather on Telegram).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/url-encoding-bot.git
   cd url-encoding-bot
   ```

2. Install dependencies:
   ```bash
   pip install pyrogram
   ```

3. Set up your bot credentials in the script:
   - Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_BOT_TOKEN` with your actual Telegram bot credentials.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests with enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
**Note:** Ensure your bot's token and API keys are kept secure and not shared publicly.
