from pyrogram import Client, filters
import urllib.parse

# Telegram Bot token from BotFather
API_ID = "YOUR_API_ID"  # You can get this from my.telegram.org
API_HASH = "YOUR_API_HASH"  # You can get this from my.telegram.org
BOT_TOKEN = "YOUR_BOT_TOKEN"  # BotFather's token

# Initialize Pyrogram Client
app = Client("url_encoder_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to encode a string to URL format
def encode_url(text):
    return urllib.parse.quote_plus(text)

# Automatically encode any message received
@app.on_message(filters.text & ~filters.edited)
def send_encoded_url(client, message):
    # Get the text of the message
    query = message.text.strip()

    if query:
        encoded_url = encode_url(query)
        response = f"Encoded URL: `{encoded_url}`"
    else:
        response = "Please send text to encode."

    # Send the encoded URL back to the user
    message.reply(response, quote=True)

# Run the bot
app.run()
