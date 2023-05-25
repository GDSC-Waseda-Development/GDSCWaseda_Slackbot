# Slack bot for GDSC Waseda

## Getting Started

Add `.env` file into the directory to set the slack tokens. Or you can add it in your gloabl environment variables. But please make sure not to expose the slack tokens in any public places.

here is the example of `.env` file.

```bash
SLACK_BOT_TOKEN=INPUT_BOT_TOKEN_HERE
SLACK_API_TOKEN=INPUT_API_TOKEN_HERE
```
### Attention

The bot are running at socket mode now, which means if you run the program, the bot will be actually running so it will react to the messages in the channel. So please make sure your changing is suitable for running.

### Prerequisites

It is recommend to use a virtual environment of Python to develop. After you switched to the virtual environment

```bash
pip install -r requirements.txt
```

to install used packages.

