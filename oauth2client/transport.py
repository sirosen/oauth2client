"""Generic Interface for Transport Layer Communications

For now, just a shim to use requests and maybe build upon in the future.
"""

import requests


class HTTPWrapper(object):
    def __init__(self):
        self.headers = {}

    def add_headers(self, headerdict):
        self.headers.update(headerdict)

    def request(self, uri, method='GET', body=None, headers=None):
        if not body:
            body = ''
        localheaders = self.headers.copy()
        if headers:
            localheaders.update(headers)

        response = requests.request(method, uri, data=body,
                                    headers=localheaders)
        response.status = response.status_code

        return response, response.content
