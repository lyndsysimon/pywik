import json

from nose.tools import *
import responses

from pywik.api import ApiConnection
from tests import PywikTestCase


class ApiTestCase(PywikTestCase):

    def setUp(self):
        self.api = ApiConnection(
            url='http://example.test',
            token_auth='abc',
        )

    @responses.activate
    def test_version(self):
        self.add_fake_response('API', 'getPiwikVersion', {"value":"2.7.0"})

        response = self.api.get(
            module='API',
            method='getPiwikVersion',
        )

        assert_equal(
            response,
            {'value': '2.7.0'}
        )
