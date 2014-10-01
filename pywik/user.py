import datetime
class User(object):

    def __init__(self, login=None, email=None, **kwargs):
        self.login = login
        self.email = email
        self.alias = kwargs.get('alias')
        self.token_auth = kwargs.get('token_auth')
        self.is_superuser = kwargs.get('is_superuser')
        self.date_registered = kwargs.get('date_registered')

    def __eq__(self, other):
        return self.login == other.login

    @classmethod
    def from_dict(cls, data):
        user = User()
        user.login = data['login']
        user.email = data['email']
        user.alias = data['alias']
        user.token_auth = data['token_auth']
        user.is_superuser = int(data['superuser_access']) > 0
        user.date_registered = datetime.datetime.strptime(
            data['date_registered'],
            '%Y-%m-%d %H:%M:%S'
        )

        return user