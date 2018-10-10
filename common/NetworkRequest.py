import requests
import json
import config
import re
from tool.Tool import Tool


class NetworkRequest:
    def __init__(self):
        self.req = requests.session()
        self.baseUrl = config.baseUrl
        self.cookies = None
        self.response = None
        self.token = None
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X - Requested - With': "XMLHttpRequest",
            'X-CSRF-TOKEN': ""
        }

    # ****************************************************

    def get_headers(self):
        return self.headers

    def del_headers(self, key):
        self.headers.pop(key)

    def set_headers(self, key, val):
        self.headers[key] = val

    # ****************************************************

    def post(self, url, data=None, headers=None, cookies=None):
        if headers is None:
            post_headers = self.headers
        else:
            post_headers = headers
        self.response = self.req.post(self.baseUrl + url, data=data, headers=post_headers)
        return self.response

    def get(self, url, data=None, headers=None, cookies=None):
        if headers is None:
            post_headers = self.headers
        else:
            post_headers = headers
        self.response = self.req.get(self.baseUrl + url, data=data, headers=post_headers)
        return self.response
    # ****************************************************

    def request_token(self):
        try:
            result = self.req.get(self.baseUrl+'/login',headers=self.headers)
            page_info = result.text
            token = re.findall(r'name="csrf-token" content="(.*?)">', str(page_info))[0]  # 正则表达式只能匹配str
            self.headers["X-CSRF-TOKEN"] = token
            return token
        except Exception as e:
            print(e)
            Tool.log(e, 'debug.log')
