from flask import Blueprint, jsonify, request, abort, make_response
from models import todos_sqlite

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos_sqlite.select_all('todos'))


@api.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or 'title' not in request.json:
        abort(400)
    todo = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    todos_sqlite.add_to_table('todos', **todo)
    return jsonify({'todo': todo}), 201


@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos_sqlite.get_record_by_id('todos', todo_id)
    if not todo:
        abort(404)
    return jsonify({"todo": todo})


@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = todos_sqlite.get_record_by_id('todos', todo_id)
    if not todo:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), int)
    ]):
        abort(400)
    todo = {
        'title': data.get('title', todo['title']),
        'description': data.get('description', todo['description']),
        'done': data.get('done', todo['done'])
    }
    todos_sqlite.update_record_by_id('todos', todo_id, **todo)
    return jsonify({'todo': todo})


@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    result = todos_sqlite.delete_record_by_id('todos', todo_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@api.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)
