
# Aaru ChatBot

Aaru ChatBot is an AI-powered Telegram bot designed to enhance user interactions through intelligent responses, automation, and seamless integrations. Built with Python, MongoDB, and Pyrogram, it provides a fast, secure, and extensible chat experience.

## Features

- **AI-Powered Conversations**: Engage users with smart, responsive dialogue.
- **Automation**: Simplify tasks with automated workflows.
- **MongoDB Integration**: Efficiently store and manage data.
- **Fast & Secure**: Leveraging Pyrogram for performance and reliability.
- **Customizable**: Easily extend functionality with custom commands.

## Deployment


### Heroku Deployment

Click the button below to deploy Aaru ChatBot on Heroku.
If You show any error like failed to app Creation Then fork and deploy

<a href="https://dashboard.heroku.com/new?template=https://github.com/CodeSearchDev/AaruChatBot">
<img src="https://img.shields.io/badge/Deploy%20On%20Heroku-008080?style=for-the-badge&logo=heroku" width="200"/>
</a>


### Deploy on Koyeb

The fastest way to deploy using Docker Compose is with Koyeb.
Click the button below to start deployment instantly.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=https://github.com/CodeSearchDev/AaruChatBot)


## Configuration

### Environment Variables
Set the following environment variables before running the bot:



#### Required
```
API_ID=<Your API ID>              # From https://my.telegram.org/apps
API_HASH=<Your API Hash>          # From https://my.telegram.org/apps
BOT_TOKEN=<Your Bot Token>        # From https://t.me/BotFather
MONGO_URL=<Your MongoDB URL>      # From https://cloud.mongodb.com
AUTH_CHANNEL=<Your Channel ID>    # Telegram channel ID for authentication
OWNER_ID=<Your Telegram User ID>  # Bot owner's Telegram ID
```

#### Optional
```
FSUB=false                        # Enable forced subscription (true/false)
```

## Manual Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/CodeSearchDev/AaruChatBot.git
   cd AaruChatBot
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Bot**  
   ```bash
   python3 ChatBot 
   ```

## Usage

- `/start`: Initiate the bot.
- **Admin Commands**: Manage settings and configurations.
- **AI Chat**: Interact with intelligent responses.

## Contributing

Contributions are welcome. To contribute:  
1. Fork the repository.  
2. Create a feature branch.  
3. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).