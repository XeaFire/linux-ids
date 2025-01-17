from .json_manager import JsonManager
import re
import requests

class BonusManager:
    def SendDiscordAlert(msg : str):
        config = JsonManager.Parse("ids-config.json")
        pattern = re.compile("/discordapp.com\/api\/webhooks\/([^\/]+)\/([^\/]+)/")
        print(config["discord-webhook"])
        if not pattern.match(config["discord-webhook"]):
            print("ben")
            return
        print("LowTaperfade")
        webhook = config["discord-webhook"]
        data = {"content": msg}
        requests.post(webhook, json=data)



