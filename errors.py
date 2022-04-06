# Validate error
import errno
from xmlrpc.client import Server

from werkzeug.exceptions import HTTPException

class ServerError(Exception):
    def __init__(self, msg) -> None:
        self.errno = -1
        self.errmsg = msg or ''
    pass

class LoginError(ServerError):
    errno = 101

class JsonFormError(ServerError):
    errno = 102


