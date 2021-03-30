
import os
from slack_sdk.web import WebClient
from slack_sdk.rtm.v2 import RTMClient
from slack_sdk.errors import SlackApiError


slack_token = "[API_TOKEN]"
slack_bot_token = "[BOT_API_TOKEN]"

rtm = RTMClient(token=slack_bot_token)
@rtm.on("message")
def handle(client: RTMClient, event: dict):
    print(event)
    client = WebClient(token=slack_token)
    try:
        response = client.chat_postMessage(channel='#general', text="Hello world!")
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

print("Bot is up and running!")
rtm.start()
