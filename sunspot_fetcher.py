import requests
import json
import pandas as pd
from data_fetcher import DataFetcher
from create_logger import create_logger
from settings.base import API, API_KEY

# TODO: Add tests, add checks for a 200

headers = {
    'Content-Type': 'application/json'
}


class SunspotFetcher(DataFetcher):
    """Fetches sunspot data.
    """

    def __init__(self, api, api_key):
        DataFetcher.__init__(self, api_key)
        self.api = api
        self.api_key = api_key
        self.request_to_format = self.api

    def get_column_names(self):
        """Get column names from api.
        """
        if not self.response:
            self.get(self.api_key)
        column_names = self.response.json().get('dataset').get('column_names')
        return column_names
    
    def get_data(self):
        """Get dataset
        """
        if not self.response:
            self.get(api_key)
        dataset = self.response.json().get('dataset').get('data')
        return dataset

    def pandas(self):
        """Calls get_data and get_column_names and creates a pandas dataframe.
        """
        if not self.response:
            self.get(self.api_key)
        column_names = self.get_column_names()
        dataset = self.get_data()
        return pd.DataFrame(dataset, columns=column_names)
        

def get_sunspots():
    logger = create_logger()
    daily_sunspots = SunspotFetcher(api=API, api_key=API_KEY)
    response = daily_sunspots.get()
    df = daily_sunspots.pandas() 
    logger.info(df.head())
    logger.info(response.status_code)
    return df

    
if __name__ == "__main__":
    get_sunspots()
