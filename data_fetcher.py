import requests
import pandas as pd


class DataFetcher(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self):
        payload = {'api_key': self.api_key}
        self.response = requests.get(self.request_to_format, params=payload)
        if self.response.ok != True:
            log(self.response.status_code)
        return self.response
        
    def pandas(self, api_key):
        json_response = self.get().json()
        return pd.read_json(json_response.text, orient = 'records')

