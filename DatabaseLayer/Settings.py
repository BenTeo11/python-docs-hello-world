from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localDB.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/moitAdmin/ApiModules/DatabaseLayer/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 