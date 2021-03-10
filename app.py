from flask import Flask
from views import views
from api import api
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)

try:
    os.makedirs(app.instance_path)
except OSError as error:
    print(error)

app.register_blueprint(views.general)
app.register_blueprint(api.api)

if __name__ == '__main__':
    app.run(debug=True)