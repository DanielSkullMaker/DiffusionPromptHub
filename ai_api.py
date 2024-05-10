from pydantic_settings import BaseSettings, SettingsConfigDict
import requests

class aiSettings(BaseSettings):
    AI_TOKEN: str
    AI_BOT_ID: int

    @property
    def ai_request(self, query, user):
        #return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
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
            'user': f'{user}',
            'query': f'{query}',
            'stream': False,
        }

        response = requests.post('https://api.coze.com/open_api/v2/chat', headers=headers, json=json_data)
        return response.json()

    model_config = SettingsConfigDict(env_file="aiAPI.env")

aiSetting = aiSettings()