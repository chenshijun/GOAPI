#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : ApiResponse.py
# @Desc  :
import requests
import json


class ApiResponse:
    def __init__(self, e=None, msg=None, resp=None, init_obj=None):
        # self.__error_msg = ""

        self.__request_url = ""
        self.__request_method = ""
        self.__request_header = ""
        self.__request_body = ""

        self.__api_status = 1
        # self.__response_size = ""
        self.__response_reason = ""
        self.__response_time = ""
        self.__response_header = {}
        self.__response_cookie = {}
        self.__response_text = ""
        self.__response_json = {}
        self.__response_error = ""
        self.__response_code = ""
        self.__assert_status = False

        if e:
            self.request_url = init_obj['request_url']
            self.request_method = init_obj['method']
            self.request_header = init_obj['headers']
            self.api_status = -1
            self.response_error = str(e)

        if resp is not None:
            if len(resp.history):
                self.request_url = resp.history[0].url
            else:
                self.request_url = resp.url
            self.response_header = dict(resp.headers)
            self.response_reason = resp.reason
            self.response_code = resp.status_code
            self.response_time = int(resp.elapsed.total_seconds() * 1000)
            self.response_text = resp.text
            try:
                self.response_json = json.loads(resp.text)
            except:
                self.response_json = None

            for key, value in requests.utils.dict_from_cookiejar(resp.cookies).items():
                self.response_cookie[key] = value

    def get_result(self):
        if isinstance(self.request_body, dict):
            self.request_body = json.dumps(self.request_body)
        return {
            # "error_msg": self.__error_msg,
            "request_url": self.request_url,
            "request_method": self.request_method,
            "request_header": self.request_header,
            "request_body": self.request_body,
            "api_status": self.api_status,
            "response_reason": self.response_reason,
            "response_time": self.response_time,
            "response_header": self.response_header,
            "response_cookie": self.response_cookie,
            "response_text": self.response_text,
            "response_json": self.response_json,
            "response_error": self.response_error,
            "response_code": self.response_code,
            "assert_status": self.assert_status
        }

    @property
    def request_url(self):
        """
        请求链接
        """
        return self.__request_url

    @request_url.setter
    def request_url(self, url):
        self.__request_url = url

    @property
    def request_method(self):
        """
        请求方法
        """
        return self.__request_method

    @request_method.setter
    def request_method(self, method):
        self.__request_method = method

    @property
    def request_header(self):
        """
        请求头信息
        """
        return self.__request_header

    @request_header.setter
    def request_header(self, param):
        self.__request_header = param

    @property
    def request_body(self):
        """
        请求内容
        """
        return self.__request_body

    @request_body.setter
    def request_body(self, param):
        self.__request_body = param

    @property
    def assert_status(self):
        """
        """
        return self.__assert_status

    @assert_status.setter
    def assert_status(self, param):
        self.__assert_status = param

    @property
    def api_status(self):
        """
        :return -1 (接口错误)
        :return 0 (检查点错误)
        :return 1 (接口正常)
        """
        return self.__api_status

    @api_status.setter
    def api_status(self, param):
        self.__api_status = param

    # @property
    # def response_size(self):
    #     """
    #     返回内容大小
    #     """
    #     return self.__response_size
    #
    # @response_size.setter
    # def response_size(self, param):
    #     self.__response_size = param

    @property
    def response_reason(self):
        """
        返回HTTP响应的描述：OK、Not Found、等
        """
        return self.__response_reason

    @response_reason.setter
    def response_reason(self, param):
        if param:
            self.__response_reason = param
        else:
            self.__response_reason = "OK"

    @property
    def response_time(self):
        """
        耗时
        """
        return str(self.__response_time) + " ms"

    @response_time.setter
    def response_time(self, param):
        self.__response_time = param

    @property
    def response_header(self):
        """
        返回头信息
        """
        return self.__response_header

    @response_header.setter
    def response_header(self, param):
        self.__response_header = param

    @property
    def response_cookie(self):
        """
        返回cookie
        """
        return self.__response_cookie

    @response_cookie.setter
    def response_cookie(self, param):
        self.__response_cookie = param

    @property
    def response_text(self):
        """
        返回的内容
        """
        return self.__response_text

    @response_text.setter
    def response_text(self, param):
        self.__response_text = param

    @property
    def response_json(self):
        """
        返回的内容
        """
        return self.__response_json

    @response_json.setter
    def response_json(self, param):
        self.__response_json = param

    @property
    def response_error(self):
        """
        错误内容
        """
        return self.__response_error

    @response_error.setter
    def response_error(self, param):
        self.__response_error = param

    @property
    def response_code(self):
        """
        返回HTTP响应的状态码：200、404、500、等
        """
        return self.__response_code

    @response_code.setter
    def response_code(self, param):
        self.__response_code = param
