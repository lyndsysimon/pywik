from nose.tools import *
import responses

from pywik import Server
from tests import PywikTestCase


class ServerTestCase(PywikTestCase):

    def setUp(self):
        self.server = Server(url='http://example.test', token_auth='abc')

    @responses.activate
    def test_version(self):
        self.add_fake_response('API', 'getPiwikVersion', {"value":"2.7.0"})

        assert_equal(
            self.server.version,
            '2.7.0',
        )