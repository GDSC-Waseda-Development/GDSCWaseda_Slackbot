from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = "SLACK_BOT_TOKEN"
SLACK_API_TOKEN = "SLACK_API_TOKEN"

app = App(token=os.environ.get(SLACK_BOT_TOKEN))

@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

@app.message("See you!")
def message_see_you(message, say):
    say(f"See you! <@{message['user']}>!")


# Handler must be defined above this or it cannot be used
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get(SLACK_API_TOKEN)).start()