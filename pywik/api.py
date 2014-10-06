import json

import requests


class ApiConnection(object):
    def __init__(self, url, token_auth):
        self.url = url
        self.token_auth = token_auth

    def get(self, module, method):
        response = requests.get(self.url, params={
            'token_auth': self.token_auth,
            'module': module,
            'method': '{0}.{1}'.format(module, method),
            'format': 'json'
        })

        return response.json()
