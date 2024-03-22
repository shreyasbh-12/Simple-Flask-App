from flask import Flask
from app.config import Config


# Initialize app 
app = Flask(__name__)
app.config.from_object(Config)

from app import routes