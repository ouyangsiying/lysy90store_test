import requests
import hashlib
import re


class main:
    def __init__(self):
        self.url = 'http://121.199.58.28'
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X - Requested - With': "XMLHttpRequest",
            'X-CSRF-TOKEN': ""
        }
        self.s = requests.session()
        # self.headers = self.s.update(self.headers)

    def login(self, username, password):
        parm = {}
        parm["user_name"] = username
        token = self.get_token()
        self.headers["X-CSRF-TOKEN"] = token
        print(token)
        parm['_token'] = token
        parm['password'] = self.hash_password(password, token)
        try:
            result = self.s.post(self.url + '/login', data=parm, headers=self.headers)
            result2 = self.s.get(self.url + '/cart/list?page=1',  headers=self.headers)
            # print(self.headers)
            print(result2.text)
        except Exception as e:
            print(e)

    def get_token(self):
        try:
            result = self.s.get(self.url + '/login', headers=self.headers)
            page_info = result.text
            token = re.findall(r'name="csrf-token" content="(.*?)">', str(page_info))[0]  #正则表达式只能匹配str
            # token = token[0]
            # print(token)
            return token
        except Exception as e:
            print(e)

    def hash_password(self, password, token):
        hash_password1 = hashlib.sha1((password).encode('utf_8')).hexdigest()
        hash_password = hashlib.sha1((hash_password1 + token).encode('utf_8')).hexdigest()
        return hash_password


# main().get_token()
main().login('test_cs4', '111111')
