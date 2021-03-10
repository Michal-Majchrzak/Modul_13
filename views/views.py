from flask import Blueprint, request, render_template, redirect, url_for
from forms import TodoForm
from models import todos_sqlite

general = Blueprint('general', __name__, url_prefix='/todos')


@general.route('/', methods=['GET', 'POST'])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            data_for_db = {}
            for key, value in form.data.items():
                if key != 'csrf_token':
                    data_for_db[key] = value
            todos_sqlite.add_to_table('todos', **data_for_db)
        return redirect(url_for("general.todos_list"))

    todos = todos_sqlite.select_all('todos')
    return render_template("todos.html", form=form, todos=todos, error=error)


@general.route("/<int:todo_id>", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos_sqlite.get_record_by_id('todos', todo_id)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            data_for_db = {}
            for key, value in form.data.items():
                if key != 'csrf_token':
                    data_for_db[key] = value
            todos_sqlite.update_record_by_id('todos', todo_id, **data_for_db)
        return redirect(url_for("general.todos_list"))

    if not todo:
        return redirect(url_for('general.todos_list'))
    return render_template("todo.html", form=form, todo_id=todo_id)
