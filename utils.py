from flask import request
from errors import *

def json_response(data=None, code=None, errmsg=None):
    response = {}
    response['errno'] = code or 0
    response['errmsg'] = errmsg or ''
    response['data'] = data or ''
    return response