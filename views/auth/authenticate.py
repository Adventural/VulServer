import json
from flask import request, session, jsonify
from flask.views import MethodView

#coding=utf-8
class ReturnCode:
    def __init__(self):
        pass
    SUCCESS = 0
    FAILED = 100
    RESOURCE_NOT_EXISTS = 404
    UNAUTHORIZED = 403
    INTERVAL_SERVER_ERROR = 500
    BROKEN_AUTHORIZED_DATA = 501
    WRONG_PARAMS = 101

    @classmethod
    def errmsg(cls, code):
        if code == cls.SUCCESS:
            return ''
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARAMS:
            return 'wrong params'
        elif code == cls.RESOURCE_NOT_EXISTS:
            return 'resource_not_exists'
        elif code == cls.INTERVAL_SERVER_ERROR:
            return 'interval server error'
        elif code == cls.BROKEN_AUTHORIZED_DATA:
            return 'broken_authorized_data'
        else:
            return 'unknow error'

class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, errmsg=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not errmsg:
            errmsg = ReturnCode.errmsg(code)
        if data:
            response['data'] = data
        else:
            response['data'] = ''
        response['errno'] = code
        response['errmsg'] = errmsg
        return response

class AuthenticateView(MethodView, CommonResponseMixin):
    # 登录
    def post(self):
        """
        管理员登录
        ---
        tags:
        - 管理员接口
        parameters:
        - name: body
          in: body
          required: true
          schema:
            id: dto.authenticate_input
            properties:
              username:
                type: string
                description: 账户
              password:
                type: string
                description: 密码
        responses:
          '200':
            description: SUCCESS
            schema:
              id: dto.authenticate_output
              properties:
                errno:
                  type: integer
                  description: errno
                  default: 0
                errmsg:
                  type: string
                  description: response_message
                data:
                  type: object
                  description: response_data
                  properties:
                    token:
                      type: string
                      description: token
        """
        print("dasd")
        body_data = json.loads(request.get_data().decode())
        username = body_data['username']
        password = body_data['password']
        print("dasd")
        if not username or not password:
            response_data = self.wrap_json_response(errmsg="Lost require params of username or password !", code=ReturnCode.WRONG_PARAMS)
        elif username != "admin" or password != "123456":
            response_data = self.wrap_json_response(errmsg="Authentication Failed !!!", code=ReturnCode.BROKEN_AUTHORIZED_DATA)
        else:
            session['admin'] = 'A1akPTQJiz9wi9yo4rDz8ubM1b1'
            data = {"token": session['admin']}
            response_data = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        return jsonify(response_data)