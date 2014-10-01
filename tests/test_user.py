from nose.tools import *

from pywik import User
from tests import PywikTestCase


class UserTestCase(PywikTestCase):

    def test_from_dict(self):
        user = User.from_dict({
            'login': 'admin',
            'password': '01e6b375cab45dd3f9ae15a417aee257',
            'alias': 'Test User 0',
            'email': 'admin@example.org',
            'token_auth': '6a110eba31b4424558fb00c2a76f7380',
            'superuser_access': '1',
            'date_registered': '2014-09-30 17:39:38'
        })

        assert_equal('admin', user.login)