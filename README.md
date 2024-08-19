# URLGuardian Discord Bot

URLGuardian is a Discord bot designed to protect your server by scanning and removing suspicious URLs posted in chat. It uses the VirusTotal API to analyze links and take action against potentially malicious content, keeping your community safe.

## Pre-requisites

- **Discord Developer API Key**
- **VirusTotal API Key**

## Obtaining API Keys

### Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **"New Application"** and give your bot a name.
3. Navigate to the **"Bot"** section in the left-hand menu.
4. Click **"Add Bot"** and confirm by clicking **"Yes, do it!"**.
5. Under the **"Token"** section, click **"Copy"** to copy your bot token. You'll use this token in your `main.py` file.
6. Ensure your bot has the necessary permissions:
   - Scroll down to **"OAuth2"** -> **"URL Generator"**.
   - Under **"Scopes"**, select **"bot"**.
   - Under **"Bot Permissions"**, select the necessary permissions for your bot (e.g., **"Read Messages"**, **"Send Messages"**, **"Manage Messages"**).
7. Use the generated URL to invite your bot to your server.
8. Enable all three **Privileged Gateway Intents**
   
   ![image](https://github.com/user-attachments/assets/c5868f6b-4b39-4000-b8a2-fec48ad51fd4)


### VirusTotal API Key

1. Go to the [VirusTotal website](https://www.virustotal.com/).
2. Sign up for a free account if you don't already have one.
3. After logging in, navigate to your [API Key](https://www.virustotal.com/gui/user/[YourUsername]/apikey) section.
4. Copy the API key provided on that page.
5. Use this key in your `apikeys.py` file.

## Installation

1. **Install the required Python packages:**

   ```bash
   pip install discord requests
   
2. **Create an `apikeys.py` file in the root directory and add your VirusTotal API key & Discord Token:**
   
   ```bash
   VT_API_KEY = "your_virustotal_api_key_here"
   TOKEN = "your_discord_bot_token_here"

3. **Run the bot**

   ```bash
   python main.py

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any changes, improvements, or bug fixes.

## Acknowledgements

  [VirusTotal API](https://www.virustotal.com/) for providing the URL scanning service.
  [Discord.py](https://discordpy.readthedocs.io/en/stable/) for the Python wrapper for the Discord API.


## **Project Structure**

  ```graphql
  URLGuardian/
    │
    ├── main.py          # The main bot script
    ├── url_extractor.py # Script for extracting URLs from messages
    ├── url_scanner.py   # Script for scanning URLs using VirusTotal API
    └── apikeys.py       # API keys file (to be created by the user)
