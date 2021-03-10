from flask import Flask, jsonify, make_response
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecret'

app.register_blueprint(views.general)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


if __name__ == '__main__':
    app.run(debug=True)