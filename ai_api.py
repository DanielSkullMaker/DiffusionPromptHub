import json

from pydantic_settings import BaseSettings, SettingsConfigDict
import requests

class aiSettings(BaseSettings):
    query: str = ""
    user: str = ""

    AI_TOKEN: str
    AI_BOT_ID: int
    model_config = SettingsConfigDict(env_file="aiAPI.env")

    @property
    def request(self) -> dict:
        headers = {
            'Authorization': f'Bearer {self.AI_TOKEN}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'api.coze.com',
            'Connection': 'keep-alive',
        }

        json_data = {
            'conversation_id': '123',
            'bot_id': f'{self.AI_BOT_ID}',
            'user': f'{self.user}',
            'query': f'{self.query}',
            'stream': False,
        }

        response = requests.post('https://api.coze.com/open_api/v2/chat', headers=headers, json=json_data)
        return response.json()

    def parser(self):
        json_request = self.request
        retMessage = []
        for i in range(0, len(json_request['messages'])):
            if i != 1:
                retMessage.append(json_request['messages'][i]['content'])
        return retMessage

"""userAI = "Nick"
print("Введите сообщение:")
quAI = input()

print(aiSettings(user=userAI, query=quAI).parser())"""