from dotenv import load_dotenv
import os
from pyrogram import Client, filters
import urllib.parse

# Load environment variables from the .env file
load_dotenv()

# Get the variables from the environment
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Check if the variables are loaded correctly
if not all([API_ID, API_HASH, BOT_TOKEN]):
    print("Error: Missing environment variables. Please check your .env file.")
    exit(1)

# Initialize Pyrogram Client with environment variables
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

