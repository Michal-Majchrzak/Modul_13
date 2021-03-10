from flask import Flask
from views import views
from api import api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecret'

app.register_blueprint(views.general)
app.register_blueprint(api.api)


if __name__ == '__main__':
    app.run(debug=True)