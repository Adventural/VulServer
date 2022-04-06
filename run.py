from pkgutil import ImpImporter
from gevent import pywsgi
from app import app
from errors import *
from views.auth import admin

# Admin router
app.register_blueprint(admin)

if __name__ =="__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 9777), app)
    server.serve_forever()