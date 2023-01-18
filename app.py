from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import jsonhandle
import json
import requests
import  os
app = Flask(__name__)

line_bot_api = LineBotApi('<Channel_Access_Token>')
handler = WebhookHandler('<Channel_Secret>')
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

#=======偵測訊息


@handler.add(MessageEvent, message=TextMessage)
def ReplyPrice(event):
    jsonhandle.jsonget(query=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(jsonhandle.stockxTitle,jsonhandle.productmsg)
        )



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)