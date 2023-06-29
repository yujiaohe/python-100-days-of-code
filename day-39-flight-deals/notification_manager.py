import requests
import os
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem

ACCESS_TOKEN = os.environ.get("GUA_TOKEN")
SECRET = os.environ.get("GUA_SECRET")
WEBHOOK = f"https://oapi.dingtalk.com/robot/send?access_token={ACCESS_TOKEN}"


class NotificationManager:

    def __init__(self):
        self.xiaoding = DingtalkChatbot(WEBHOOK, secret=SECRET)

    def send_sms(self, message):
        self.xiaoding.send_text(msg=message, is_at_all=True)


