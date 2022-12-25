import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "lobby", "soccer", "basketball",  "baseball",  "soccer_player", "basketball_player",  "baseball_player", "soccer_player_Messi","soccer_player_Neymar","soccer_player_Pogba","soccer_player_Mbappe","soccer_player_Ronaldo","soccer_player_Modric", "basketball_player_Durant", "basketball_player_Irving", "basketball_player_Harden", "basketball_player_George", "basketball_player_Curry", "baseball_player_Judge", "baseball_player_Betts", "baseball_player_Stanton", "baseball_player_Harper", "baseball_player_Cole"],
    transitions=[
        {
            "trigger"    : "advance",
            "source"     : "user",
            "dest"       : "lobby",
            "conditions" : "is_going_to_lobby",
        },
        {
            "trigger"    : "advance",
            "source"     : "lobby",
            "dest"       : "soccer",
            "conditions" : "is_going_to_soccer",
        },
        {
            "trigger"    : "advance",
            "source"     : "lobby",
            "dest"       : "baseball",
            "conditions" : "is_going_to_baseball",
        },
        {
            "trigger"    : "advance",
            "source"     : "lobby",
            "dest"       : "basketball",
            "conditions" : "is_going_to_basketball",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Messi",
            "conditions" : "is_going_to_soccer_player_Messi",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Neymar",
            "conditions" : "is_going_to_soccer_player_Neymar",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Pogba",
            "conditions" : "is_going_to_soccer_player_Pogba",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Mbappe",
            "conditions" : "is_going_to_soccer_player_Mbappe",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Ronaldo",
            "conditions" : "is_going_to_soccer_player_Ronaldo",
        },
        {
            "trigger"    : "advance",
            "source"     : "soccer",
            "dest"       : "soccer_player_Modric",
            "conditions" : "is_going_to_soccer_player_Modric",
        },
        {
            "trigger"    : "advance",
            "source"     : "basketball",
            "dest"       : "basketball_player_Durant",
            "conditions" : "is_going_to_basketball_player_Durant",
        },
        {
            "trigger"    : "advance",
            "source"     : "basketball",
            "dest"       : "basketball_player_Harden",
            "conditions" : "is_going_to_basketball_player_Harden",
        },
        {
            "trigger"    : "advance",
            "source"     : "basketball",
            "dest"       : "basketball_player_Irving",
            "conditions" : "is_going_to_basketball_player_Irving",
        },
        {
            "trigger"    : "advance",
            "source"     : "basketball",
            "dest"       : "basketball_player_George",
            "conditions" : "is_going_to_basketball_player_George",
        },
        {
            "trigger"    : "advance",
            "source"     : "basketball",
            "dest"       : "basketball_player_Curry",
            "conditions" : "is_going_to_basketball_player_Curry",
        },
        {
            "trigger"    : "advance",
            "source"     : "baseball",
            "dest"       : "baseball_player_Judge",
            "conditions" : "is_going_to_baseball_player_Judge",
        },
        {
            "trigger"    : "advance",
            "source"     : "baseball",
            "dest"       : "baseball_player_Betts",
            "conditions" : "is_going_to_baseball_player_Betts",
        },
        {
            "trigger"    : "advance",
            "source"     : "baseball",
            "dest"       : "baseball_player_Stanton",
            "conditions" : "is_going_to_baseball_player_Stanton",
        },
        {
            "trigger"    : "advance",
            "source"     : "baseball",
            "dest"       : "baseball_player_Harper",
            "conditions" : "is_going_to_baseball_player_Harper",
        },
        {
            "trigger"    : "advance",
            "source"     : "baseball",
            "dest"       : "baseball_player_Cole",
            "conditions" : "is_going_to_baseball_player_Cole",
        },
        {
            "trigger"    : "go_back", 
            "source"     : "soccer", 
            "dest"       : "lobby"
        },
        {
            "trigger"    : "go_back", 
            "source"     : "baseball", 
            "dest"       : "lobby"
        },
        {
            "trigger"    : "go_back", 
            "source"     : "basketball", 
            "dest"       : "lobby"
        },
        {
            "trigger"    : "go_back_user", 
            "source"     : ["soccer_player_Messi","soccer_player_Neymar","soccer_player_Pogba","soccer_player_Mbappe","soccer_player_Ronaldo","soccer_player_Modric", "basketball_player_Durant", "basketball_player_Irving", "basketball_player_Harden", "basketball_player_George", "basketball_player_Curry", "baseball_player_Judge", "baseball_player_Betts", "baseball_player_Stanton", "baseball_player_Harper", "baseball_player_Cole"], 
            "dest"       : "user"
            #"conditions" : "is_going_back_to_lobby",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        print("test")
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
        # print(event.message.text)
        # print("terst")
        response = machine.advance(event)
        # print(response)

        if response == False:
            #reply_token=
            #sticker_message=StickerSendMessage(
            #    package_id='6632',
            #    sticker_id='11825378'
            #)
            #line_bot_api.reply_message(reply_token, sticker_message)
            
            send_text_message(event.reply_token, "Not Entering any State,please try again")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    print("fdfdf")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
