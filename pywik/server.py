from .api import ApiConnection


class Server(object):

    __version = None

    @property
    def version(self):
        if not self.__version:
            self.__version = self._api.get(
                module='API',
                method='getPiwikVersion'
            )['value']

        return self.__version

    def __init__(self, url, token_auth):
        self._api = ApiConnection(url=url, token_auth=token_auth)