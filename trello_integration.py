# loading the required libraries:
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')
BASE_URL = "https://api.trello.com/1"

# creating a class for integration trello:
class TrelloIntegration:
    def __init__(self):
        self.auth_params = {
            'key': API_KEY,
            'token': TOKEN
        }

    def create_card(self, list_id, card_name, description=""):
        url = f"{BASE_URL}/cards"
        params = {
            **self.auth_params,
            'name': card_name,
            'desc': description,
            'idList': list_id
        }
        response = requests.post(url, params=params)
        return response.json()

    def get_list_cards(self, list_id):
        url = f"{BASE_URL}/lists/{list_id}/cards"
        params = self.auth_params
        response = requests.get(url, params=params)
        return response.json()