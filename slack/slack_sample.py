#import slack_client
from slackclient import SlackClient
#import time, for waiting
import time

#instantiate a new slack_client object
sc = SlackClient("xoxp-223543408598-222652276210-222005906880-1c087b0cff1eac7df112dfb4a43a50e7")

#send a webrequest as an api_call
sc.api_call("channels.list")

sc.api_call("users.list")

#send message to channel #general
sc.api_call(
"chat.postMessage",
channel="#general",
text="Hello from Python-ICT Course!"
)

#recieve messages
if sc.rtm_connect():
    while True:
        print (sc.rtm_read())
        time.sleep(1)
else:
    print ("Connection Failed, invalid token?")


