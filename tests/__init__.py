import json
import unittest

import responses


class PywikTestCase(unittest.TestCase):

    def add_fake_response(self, module, method, value, http_method='get', status=200):
        responses.add(
            getattr(responses, http_method.upper()),
            'http://example.test/?'
                'module={module}'
                '&method={module}.{method}'
                '&format=json'
                '&token_auth=abc'.format(
                    module=module,
                    method=method
                ),
            match_querystring=True,
            body=json.dumps(value),
            content_type='application/json',
            status=200,
        )