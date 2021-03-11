from flask import render_template, Blueprint
from app.models import Reader

readers = Blueprint('readers', __name__, url_prefix='/readers')


@readers.route('/list', methods=['GET'])
def render_readers_list():
    readers_list = Reader.query.all()
    return render_template('/reader/readers_list.html', readers_list=readers_list)
