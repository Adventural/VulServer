import config
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from errors import *

app = Flask(__name__)

# Database
app.config.from_object(config)
db=SQLAlchemy(app)

# Index router
@app.route('/')
def start():
    pass

# Before request
@app.before_request
def process_request(*args,**kwargs):
    # print('before '+ request.path)
    pass

# After request
@app.after_request
def process_request(response):
    return response

# Handle base http error
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    # r = e.get_response()
    response = {}
    response['errno'] = e.code
    response['errmsg'] = e.description
    response['data'] = ''
    return response

@app.errorhandler(ServerError)
def handle_validerror(e):
    response = {}
    response['errno'] = e.errno
    response['errmsg'] = e.errmsg
    response['data'] = ''
    return response
