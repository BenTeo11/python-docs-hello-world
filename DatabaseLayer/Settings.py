from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
#from logging.config import dictConfig
#from logging.handlers import SMTPHandler
import pyodbc
import urllib.parse

params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:apiservice.database.windows.net,1433;Database=ApiService;Uid=apiserviceAdmin;Pwd=BenTeo18062416;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#local DB

# from flask import Flask

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localDB.db'
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/moitAdmin/ApiModules/DatabaseLayer/database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False