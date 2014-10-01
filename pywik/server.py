from .api import ApiConnection
from .user import User


class Server(object):

    __users = None

    @property
    def users(self):
        if self.__users is None:
            self.__users = [
                User.from_dict(u) for u in self._api.get(
                    module='UsersManager',
                    method='getUsers',
                )
            ]

        return self.__users

    __version = None

    @property
    def version(self):
        if self.__version is None:
            self.__version = self._api.get(
                module='API',
                method='getPiwikVersion'
            )['value']

        return self.__version


    def __init__(self, url, token_auth):
        self._api = ApiConnection(url=url, token_auth=token_auth)