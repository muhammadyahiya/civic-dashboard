import requests
import json


class ApiClient:

    def __init__(self):
        # self.get_data(api)

        self.root_url = "https://data.telangana.gov.in/api/1/datastore/query/"
        # self.get_user_data(api, parameters)

    def get_data(self, api):
        response = requests.get(self.root_url + api)
        if response.status_code == 200:

            return response.json()
        else:
            return False
