import requests
import json
import urllib3
from util.ApiResponse import ApiResponse
from pytest_testconfig import config

urllib3.disable_warnings()


class BaseRequest:

    def __init__(self, url_host, uri, data=None, params=None, headers={}, cookies={}, timeout=5,
                 allow_redirects=True, default_header=True, need_token=True):
        self.host = url_host
        self.uri = uri
        self.data = data
        self.params = params
        self.headers = headers
        self.cookies = cookies
        self.url = self.host + self.uri
        self.timeout = timeout
        self.allow_redirects = allow_redirects

        if default_header:
            self.headers['Content-Type'] = "application/json"
        if need_token:
            self.headers['Authorization'] = config['gHub']['authorization']

    def get(self):
        try:
            r = requests.get(self.url, params=self.params, headers=self.headers, timeout=self.timeout,
                             allow_redirects=self.allow_redirects, verify=False)
            r = ApiResponse(resp=r)
            r.request_header = self.headers
            r.request_method = "GET"
        except Exception as e:
            r = ApiResponse(e=str(e),
                            init_obj={"request_url": self.url, "method": "GET", "param": self.param,
                                      "headers": self.headers})

    def post(self):
        try:
            if "application/json" in self.headers['Content-Type'] and isinstance(self.data, dict):
                self.data = json.dumps(self.data)
            jar = requests.utils.cookiejar_from_dict(self.cookies, cookiejar=None, overwrite=True)
            r = requests.post(self.url, params=self.params, data=self.data, timeout=self.timeout,
                              allow_redirects=self.allow_redirects, headers=self.headers, cookies=jar, verify=False)
            r = ApiResponse(resp=r)
            r.request_header = self.headers
            r.request_body = self.data
            r.request_method = "POST"
        except Exception as e:
            r = ApiResponse(e=str(e), init_obj={"request_url": self.url, "method": "POST", "headers": self.headers})
        return r

    def put(self):
        try:
            if "application/json" in self.headers['Content-Type'] and isinstance(self.data, dict):
                self.data = json.dumps(self.data)
            jar = requests.utils.cookiejar_from_dict(self.cookie, cookiejar=None, overwrite=True)
            r = requests.put(self.url, params=self.param, data=self.data, timeout=self.timeout,
                             allow_redirects=self.allow_redirects, headers=self.headers, cookies=jar, verify=False)
            r = ApiResponse(resp=r)
            r.request_header = self.headers
            r.request_body = self.data
            r.request_method = "PUT"
        except Exception as e:
            r = ApiResponse(e=str(e), init_obj={"request_url": self.url, "method": "PUT", "headers": self.headers})
        return r

    def delete(self):
        try:
            r = requests.delete(self.url, params=self.params, headers=self.headers, timeout=self.timeout,
                                allow_redirects=self.allow_redirects, verify=False)
            r = ApiResponse(resp=r)
            r.request_header = self.headers
            r.request_method = "DELETE"
        except Exception as e:
            r = ApiResponse(e=str(e),
                            init_obj={"request_url": self.url, "method": "DELETE", "param": self.param,
                                      "headers": self.headers})
