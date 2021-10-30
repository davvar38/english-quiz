import os

import pandas
import requests

from io import BytesIO

from english_quiz.infrastructure.table_reader import TableReader

FILE_ID = os.getenv('FILE_ID')
API_KEY = os.getenv('API_KEY')


class TableRetriever:
    @staticmethod
    def get_table():
        content = TableRetriever._get_table_content()
        data = TableRetriever._load_content(byte_content=content)
        return TableReader(data=data)

    @staticmethod
    def _get_table_content():
        result = requests.get(
            url=f'https://www.googleapis.com/drive/v3/files/{FILE_ID}/export',
            params={
                'mimeType': 'text/csv',
                'key': API_KEY
            },
            headers={'Accept': 'application/json'}
        )
        return result.content

    @staticmethod
    def _load_content(byte_content):
        data = pandas.read_csv(BytesIO(initial_bytes=byte_content))
        return data
