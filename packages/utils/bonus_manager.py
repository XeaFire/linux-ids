from .json_manager import JsonManager
import re
import requests

class BonusManager:
    def SendDiscordAlert(msg : str):
        config = JsonManager.Parse("ids-config.json")
        pattern = re.compile("/discordapp.com\/api\/webhooks\/([^\/]+)\/([^\/]+)/")
        if not pattern.match(config["discord-webhook"]):
            return
        webhook = config["discord-webhook"]
        data = {"content": msg}
        requests.post(webhook, json=data)



