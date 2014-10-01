from nose.tools import *
import responses

from pywik import Server, User
from tests import PywikTestCase


class ServerTestCase(PywikTestCase):

    users = {
        'anonymous': {
            'login': 'anonymous',
            'password': '',
            'alias': 'anonymous',
            'email': 'anonymous@example.org',
            'token_auth': 'anonymous',
            'superuser_access': '0',
            'date_registered': '2014-09-30 17:39:38'
        },
        'admin': {
            'login': 'admin',
            'password': '01e6b375cab45dd3f9ae15a417aee257',
            'alias': 'Test User 0',
            'email': 'admin@example.org',
            'token_auth': '6a110eba31b4424558fb00c2a76f7380',
            'superuser_access': '1',
            'date_registered': '2014-09-30 17:39:38'
        }
    }

    def setUp(self):
        self.server = Server(url='http://example.test', token_auth='abc')

    @responses.activate
    def test_version(self):
        self.add_fake_response('API', 'getPiwikVersion', {"value":"2.7.0"})

        assert_equal(
            self.server.version,
            '2.7.0',
        )

    @responses.activate
    def test_users(self):
        self.add_fake_response('UsersManager', 'getUsers', [
            self.users['anonymous'],
            self.users['admin'],
        ])

        assert_equal(
            [
                User.from_dict(self.users['anonymous']),
                User.from_dict(self.users['admin']),
            ],
            self.server.users,
        )