from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
import re

channel_ids = {"backend":"C02HKKFAH8B","frontend":"whoknows"}

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

@app.event("message")
def handle_message_events(body, logger):
    pass

@app.event("app_mention")
def mention_handler(event, say):
    channel_id = event["channel"]
    if channel_id == channel_ids["backend"]:
        text = re.sub('\\s<@[^, ]*|^<@[^, ]*', '', event['text'])
        if 'check' in text:
            user_info = app.client.users_info(user=event["user"])
            user_name = user_info["user"]["profile"]["display_name"]
            say(f"Hi, Checked {user_name}")

# Handler must be defined above this or it cannot be used
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get(SLACK_API_TOKEN)).start()