from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
import re
# from google_doc import add_name
import google.generativeai as palm

channel_ids = {"backend": "C02HKKFAH8B", "frontend": "whoknows"}

load_dotenv()

SLACK_BOT_TOKEN = "SLACK_BOT_TOKEN"
SLACK_API_TOKEN = "SLACK_API_TOKEN"
PALM_API_KEY = "PALM_API_KEY"

app = App(token=os.environ.get(SLACK_BOT_TOKEN))
palm.configure(api_key=os.environ.get(PALM_API_KEY))


@app.message("hello")
def message_hello(message, say):
  # say() sends a message to the channel where the event was triggered
  say(f"Hey there <@{message['user']}>!")


@app.message("See you!")
def message_see_you(message, say):
  say(f"See you! <@{message['user']}>!")


@app.message("ask")
def ask_palm(event, say):
  print("Asking PALM....")
  text = re.sub(r'ask', '', event['text'])
  response = palm.chat(messages=[str(text)])
  # print("Response is:" + response) TODO: Coerce Response to String
  response_text: str = response.last
  say(response_text)


@app.event("message")
def handle_message_events(event, say):
  if event['channel_type'] == 'im':
    # DM
    say("You are sending message in dm!")
  elif event['channel_type'] == 'group':
    # Channel
    if event['channel'] in channel_ids['backend']:
      say("You are sending message in Backend Channel!")
      if str(event['text']).startswith('.ask'):
        ask_palm(event, say)
  # elif event["channel_type"] == 'channel':
  #   say("You are sending message in channel")
  else:
    say("I do not know where you send this message from.")


@app.event("app_mention")
def mention_handler(event, say):
  channel_id = event["channel"]
  if channel_id == channel_ids["backend"]:
    text = re.sub('\\s<@[^, ]*|^<@[^, ]*', '', event['text'])
    if 'check' in text:
      user_info = app.client.users_info(user=event["user"])
      user_name = user_info["user"]["profile"]["display_name"]
      add_name(user_name, "1W59UxNVhs2XXlAH9ckWpkY35BQ-DG5qZGdnJuEEbOAY")
      say(f"You sent: {text}")
      say(f"Hi, Checked {user_name}")


# Handler must be defined above this or it cannot be used
if __name__ == "__main__":
  SocketModeHandler(app, os.environ.get(SLACK_API_TOKEN)).start()

#Code suggested by Chat GPT

# SCOPES = ['https://www.googleapis.com/auth/documents']

# def get_authenticated_service():
#     creds = None
#     token_file = 'token.pickle'

#     # Load existing credentials if available
#     if os.path.exists(token_file):
#         with open(token_file, 'rb') as token:
#             creds = pickle.load(token)

#     # If no credentials or they are invalid, authenticate using OAuth 2.0
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)

#         # Save the credentials for future use
#         with open(token_file, 'wb') as token:
#             pickle.dump(creds, token)

#     return creds

# # Use the authenticated service to interact with Google Docs
# def interact_with_google_docs():
#     creds = get_authenticated_service()

#     # Use creds to create an authorized client for Google Docs API
#     # Replace this with your code to interact with the Google Docs API

# # Call the function to interact with Google Docs
# interact_with_google_docs()
