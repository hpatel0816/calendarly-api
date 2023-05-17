from flask import Flask
from security.secrets import secretKey, databaseURI
from .db import db

#Initializing the create_app
create_app = Flask(__name__)
create_app.config["SECRET_KEY"] = secretKey
create_app.config["MONGO_URI"] = databaseURI

# Import routes at the end to avoid circular imports
from api import routes