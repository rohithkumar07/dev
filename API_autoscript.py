import requests
import json

SERVER_IP = "https:// "
SERVER_PORT = ": "
LOGIN_DETAILS = {
    'client_id' : '',
    'client_secret' : '',
    'grant_type' : '',
    'username' : '',
    'password' : '',
    'device_id' : '',
}

(mention the post details after calling the GET request , Classes will differ from one call to another call )

URLS = {
    'login_url' : "/api_extension",
    'module_url' : '/api_extension_url',
    'module1_url' : '/api_extension_url',
}


class AutomationClass(object):
    def __init__(self):
        self.access_token = self.get_access_token()

    def error_code(self,code,data):
        error_dict= {"101": "API HTTP Failure",
                     "102": "API Data Failure",
                     }
        return ({"status":False,"code".error_dict.get(code),"data": data})

    def request_method(self,url,method= 'GET', data=None):
        headers=None
        if not url==SERVER_IP + SERVER_PORT + URLS.get('login_url'):
            headers = {"Authorization": "Bearer" + self.access_token}

        if method== 'GET':
            req_data = requests.get(url,headers=headers)
        else:
            req_data = requests.get(url,data=data, headers=headers)
        if not req_data.status_code ==200:
            return self.error_code('101', data=None)
        data = req_data.json()
        if not data.get('status'):
            return self.error_code('102', data=data)
        return data
    def get_access_token(self):
        url = SERVER_IP + SERVER_PORT + URLS.get('login_url')
        data = self.request_method(url,method='POST', data=LOGIN_DETAILS)
        if data.get("code", None):
            print("failed getting token api, error: %s" %data)
            return data
        else:
            print(data)
            return data.get('data') .get("access_token")





