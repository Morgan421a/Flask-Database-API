from flask import Flask

app = Flask(__name__)

from app import routes # imported after app to prevent circular imports